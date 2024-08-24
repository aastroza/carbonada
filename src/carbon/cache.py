import os
import json
import psycopg2
from dotenv import load_dotenv

load_dotenv()

def get_cached_results(query):
    with psycopg2.connect(os.environ["DB_CONNECTION_STRING"]) as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT results 
                FROM carbonada_cache 
                WHERE query = %s 
                  AND created_at > NOW() - INTERVAL %s
                ORDER BY created_at DESC
                LIMIT 1
            """, (query, "1 minute"))
            cached_result = cur.fetchone()
            if cached_result:
                return cached_result[0]
            return None

def cache_results(query, results):
    with psycopg2.connect(os.environ["DB_CONNECTION_STRING"]) as conn:
        with conn.cursor() as cur:
            cur.execute(
                """INSERT INTO carbonada_cache (query, results) VALUES (%s, %s)
                   ON CONFLICT (query) DO UPDATE SET results = EXCLUDED.results, created_at = CURRENT_TIMESTAMP""",
                (query, json.dumps(results))
            )

def log_results(query, results):
    with psycopg2.connect(os.environ["DB_CONNECTION_STRING"]) as conn:
        with conn.cursor() as cur:
            cur.execute(
                """INSERT INTO carbonada_log (query, results) VALUES (%s, %s)""",
                (query, json.dumps(results))
            )