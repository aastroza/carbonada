# Carbon

Our project helps people learn about their carbon footprint with a fun game powered by AI. We use LLMs to estimate the carbon impact of different things and create an engaging way to understand and care about the environment.

## Motivation

We are addressing the urgent need to increase awareness about carbon footprints. Many people do not understand the impact of their daily choices on emissions. For example, an apple generates 35g of CO2, while a portion of beef produces 7,700g.[^1] Calculating and visualizing the environmental impact is complex, and current tools are tedious and unattractive. We aim to create a fun, accessible educational experience to promote carbon literacy.

[^1]: [Clever Carbon](https://clevercarbon.io/aboutclevercarbon/)

Our project uses AI in two main components:

- *Carbon Footprint Estimation Model:* It estimates the carbon footprint of any concept entered by the user using GPT-4, function calling and semantic search.
- *Educational Game:* Players place cards on a "carbon line" based on their estimated carbon footprint. An AI agent supervises the game, ensuring fairness and evaluating the originality of each move.

Our innovative approach combines advanced AI with game mechanics to create an engaging educational experience about carbon footprints.

### What is a carbon footprint?

Mike Bernes-Lee [^2] defines the term "carbon footprint" as follows:

> I’m using “footprint” as a metaphor for the total impact that something has. And I’m using the word “carbon” as shorthand for all the different global warming greenhouse gases.
> So, I’m using the term “carbon footprint” to mean the best estimate we can get of the full climate change impact of something. That something could be anything—an activity, an item, a lifestyle, a company, a country, or even the whole world.

[^2]: Berners-Lee, M. (2022). *The carbon footprint of everything* (2nd ed.). Greystone Books.

## Exploration

### Carbon Footprint Estimation Model

To estimate the carbon footprint of a product or service, we utilize two main tables:

1. **Product Carbon Footprint Table**:
   - Contains specific data on the carbon footprint of various products from multiple sources.

   | product      | carbon footprint | source        |
   |--------------|------------------|---------------|
   | Apple        | 0.3 kg CO2e      | Source A      |
   | Banana       | 0.2 kg CO2e      | Source B      |
   | Orange       | 0.25 kg CO2e     | Source C      |

2. **Industry Carbon Footprint Table**:
   - Provides information on the carbon footprint associated with different industries based on economic value in dollars and the country.

   | industry     | carbon footprint per USD | country   | source        |
   |--------------|--------------------------|-----------|---------------|
   | Agriculture  | 0.5 kg CO2e/USD          | USA       | Source D      |
   | Manufacturing| 0.8 kg CO2e/USD          | Germany   | Source E      |
   | Transport    | 1.0 kg CO2e/USD          | China     | Source F      |

### Estimation Process

1. **Semantic Search in Product Table**:
   - When a user inputs, for example, "an apple," the model performs a semantic search in the product column.
   - It returns the row with the smallest semantic distance.
   - **Confidence Levels**:
     - High Confidence: `distance < u1`.
     - Medium Confidence: `u1 <= distance < u2`.

2. **Search in Industry Table**:
   - If the distance is greater than `u2`, the second table is used.
   - An LLM determines the relevant industry and estimates its value in USD.
   - The closest row in the Industry Carbon Footprint Table is returned.
   - The result is considered to have low confidence.

### Estimation Function

The function takes the user's input and returns:
   - The estimated carbon footprint.
   - The confidence level of the estimation (high, medium, low).
   - The source used for the estimation.

#### Example

**Input**: "an apple"

**Output**:
```json
{
  "estimated_carbon_footprint": "0.3 kg CO2e",
  "confidence_level": "high",
  "source": "Source A"
}
```

### Handling Complex Queries

For more complex queries, such as "an apple and a glass of water," we use function calling to decompose the query into individual calls to our estimation function. The final result is the aggregated response.

#### Example

**Input**: "an apple and a glass of water"

**Process**:
1. Decompose the query into "an apple" and "a glass of water".
2. Estimate the carbon footprint for each item.
3. Aggregate the results.

**Output**:
```json
{
  "items": [
    {
      "item": "apple",
      "estimated_carbon_footprint": "0.3 kg CO2e",
      "confidence_level": "high",
      "source": "Source A"
    },
    {
      "item": "glass of water",
      "estimated_carbon_footprint": "0.05 kg CO2e",
      "confidence_level": "medium",
      "source": "Source B"
    }
  ],
  "total_estimated_carbon_footprint": "0.35 kg CO2e"
}
```

## Game Design

We created an educational game styled like [*Timeline*](https://boardgamegeek.com/boardgame/128664/timeline) focused on the carbon footprint.

### Gameplay

- Players position cards with different concepts on a "carbon line" based on their estimated carbon footprint, with the least carbon-generating items on the left and the most on the right.
- For example, if an apple is on the left of the screen and a plane trip is on the right, the player needs to think of a concept like a hamburger and place it correctly between the apple and the plane trip.
- The system uses our carbon footprint estimation model to evaluate the correctness of each move.

### LLM as a Game Judge

- We implemented an AI agent to supervise the game in real-time.
- This agent detects strategies to "cheat" the system, such as multiplying concepts (e.g., "two apples").
- The agent evaluates the validity and originality of each move, blocking unfair or repetitive ones.
- In case of a block, the system asks the player to propose a new concept, keeping the game challenging and educational.

This way, we created a dynamic, fair, and educational game experience that promotes learning about the carbon footprint in an entertaining manner.

## Datasets

| Name | Author | Link |
| ---|---| ---|
| Carbon Catalogue | Christoph J Meinrenken et al | [Springer](https://springernature.figshare.com/articles/dataset/The_Carbon_Catalogue_public_database_Carbon_footprints_of_866_commercial_products_across_8_industry_sectors_and_5_continents/16908979?backTo=%2Fcollections%2FThe_Carbon_Catalogue_Carbon_footprints_of_866_commercial_products_from_8_industry_sectors_and_5_continents%2F5408100&file=31271269) |
| Idemat Database | SSIM, Delft University of Technology | [Eco Cost Value](https://www.ecocostsvalue.com/data) |
| MRIO | Small World Consulting | [SWC](https://www.sw-consulting.co.uk/mrio) |


More details about the datasets used in this project can be found [here](data/README.md).

## Team

[Alonso Astroza](https://github.com/aastroza), [Víctor Navarro](https://github.com/Vokturz), [Luis Miranda](https://github.com/totoiii), [Claudia Navarro](https://github.com/ClaudiaRayen) and [Bastián Araya](https://github.com/xSharky).

## Acknowledgment

We would like to take this opportunity to thank our mentors for their invaluable guidance and support: [Alonso Silva](https://github.com/alonsosilvaallende), [Eduardo Graells-Garrido](https://github.com/zorzalerrante), [Sergio Concha](https://cl.linkedin.com/in/sergio-concha-4032508), [Rodrigo Zigante](https://www.linkedin.com/in/rzigante/) and [Renzo Lüttges](https://x.com/renzolut).


## References