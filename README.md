# Carbon

Our project helps people learn about their carbon footprint with a fun game powered by AI. We use LLMs to estimate the carbon impact of different things and create an engaging way to understand and care about the environment.

## Motivation

We are addressing the urgent need to increase awareness about carbon footprints. Many people do not understand the impact of their daily choices on emissions. For example, an apple generates 35g of CO2, while a portion of beef produces 7,700g.[^1] Calculating and visualizing the environmental impact is complex, and current tools are tedious and unattractive. We aim to create a fun, accessible educational experience to promote carbon literacy.

[^1]: [Clever Carbon](https://clevercarbon.io/aboutclevercarbon/)

Our project uses AI in two main components:

- *Carbon Footprint Estimation Model:* It estimates the carbon footprint of any concept entered by the user using GPT-4 and semantic search.
- *Educational Game:* Players place cards on a "carbon line" based on their estimated carbon footprint. An AI agent supervises the game, ensuring fairness and evaluating the originality of each move.

Our innovative approach combines advanced AI with game mechanics to create an engaging educational experience about carbon footprints.

### What is a carbon footprint?

Mike Bernes-Lee [^2] defines the term "carbon footprint" as follows:

> “Carbon footprint” is a phrase that is horribly abused. I want to make my definition clear. Throughout this book, I’m using “footprint” as a metaphor for the total impact that something has. And I’m using the word “carbon” as shorthand for all the different global warming greenhouse gases.
> So, I’m using the term “carbon footprint” to mean the best estimate we can get of the full climate change impact of something. That something could be anything—an activity, an item, a lifestyle, a company, a country, or even the whole world.

[^2]: Berners-Lee, M. (2022). *The carbon footprint of everything* (2nd ed.). Greystone Books.

## Exploration

## Game Design

We created an educational game styled like [*Timeline*](https://boardgamegeek.com/boardgame/128664/timeline) focused on the carbon footprint.

### Gameplay

- Players position cards with different concepts on a "carbon line" based on their estimated carbon footprint, with the least carbon-generating items on the left and the most on the right.
- For example, if an apple is on the left of the screen and a plane trip is on the right, the player needs to think of a concept like a hamburger and place it correctly between the apple and the plane trip.
- The system uses our carbon footprint estimation model to evaluate the correctness of each move.

### LLM as Game Judge

- We implemented an AI agent to supervise the game in real-time.
- This agent detects strategies to "cheat" the system, such as multiplying concepts (e.g., "two apples").
- The agent evaluates the validity and originality of each move, blocking unfair or repetitive ones.
- In case of a block, the system asks the player to propose a new concept, keeping the game challenging and educational.

This way, we created a dynamic, fair, and educational game experience that promotes learning about the carbon footprint in an entertaining manner.

## Datasets

## Models

## Tools

## Team

[Alonso Astroza](https://github.com/aastroza), [Víctor Navarro](https://github.com/Vokturz), [Luis Miranda](https://github.com/totoiii), [Claudia Navarro](https://github.com/ClaudiaRayen) and [Bastián Araya](https://github.com/xSharky).

## Acknowledgment

We would like to take this opportunity to thank our mentors for their invaluable guidance and support: [Alonso Silva](https://github.com/alonsosilvaallende), [Eduardo Graells-Garrido](https://github.com/zorzalerrante), [Sergio Concha](https://cl.linkedin.com/in/sergio-concha-4032508), [Rodrigo Zigante](https://www.linkedin.com/in/rzigante/) and [Renzo Lüttges](https://x.com/renzolut).