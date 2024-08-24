# Carbonada

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

   | product      | carbon footprint [kg CO2e] | source        |
   |--------------|------------------|---------------|
   | Apple        | 0.3      | Source A      |
   | Banana       | 0.2      | Source B      |
   | Orange       | 0.25     | Source C      |

2. **Industry Carbon Footprint Table**:
   - Provides information on the carbon footprint associated with different industries based on economic value in dollars and the country.

   | industry     | carbon footprint per USD [kg CO2e/USD] | country   | source        |
   |--------------|--------------------------|-----------|---------------|
   | Agriculture  | 0.5           | USA       | Source D      |
   | Manufacturing| 0.8           | Germany   | Source E      |
   | Transport    | 1.0          | China     | Source F      |

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
  "estimated_carbon_footprint": "0.3",
  "carbon_footprint_unit": "kg CO2e",
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
      "estimated_carbon_footprint": "0.3",
      "carbon_footprint_unit": "kg CO2e",
      "confidence_level": "high",
      "source": "Source A"
    },
    {
      "item": "glass of water",
      "estimated_carbon_footprint": "0.05",
      "carbon_footprint_unit": "kg CO2e",
      "confidence_level": "medium",
      "source": "Source B"
    }
  ],
  "total_estimated_carbon_footprint": "0.35",
  "carbon_footprint_unit": "kg CO2e",
}
```

## Game Design

We have created an educational game inspired by the concept of a *carbonada*, a dish where players add ingredients—anything they can think of. The objective is to stay within a predetermined carbon footprint limit for the dish. The frontend code is available [here](https://github.com/Vokturz/carbon-front).

### Gameplay

- Each game sets a carbon footprint limit for the *carbonada* dish.
- Players take turns adding ingredients to the dish. These ingredients can be anything the player can imagine and write down.
- The system calculates the carbon footprint of each ingredient based on our carbon footprint estimation model.
- The goal is to avoid exceeding the carbon footprint limit. The player who adds an ingredient that causes the total carbon footprint to surpass the limit loses the game.

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
| RIVM | Dutch National Institute for Public Health | [RIVM](https://www.rivm.nl/documenten/database-milieubelasting-voedingsmiddelen) |


More details about the datasets used in this project can be found [here](data/README.md).

## Team

[Alonso Astroza](https://github.com/aastroza), [Víctor Navarro](https://github.com/Vokturz), [Luis Miranda](https://github.com/totoiii), [Claudia Navarro](https://github.com/ClaudiaRayen) and [Bastián Araya](https://github.com/xSharky).

## Acknowledgment

We would like to take this opportunity to thank our mentors for their invaluable guidance and support: [Alonso Silva](https://github.com/alonsosilvaallende), [Eduardo Graells-Garrido](https://github.com/zorzalerrante), [Sergio Concha](https://cl.linkedin.com/in/sergio-concha-4032508), [Rodrigo Zigante](https://www.linkedin.com/in/rzigante/) and [Renzo Lüttges](https://x.com/renzolut).

## Installation

To get started with running the code in this repository, please refer to our [Installation Guide](docs/installation.md).

## References