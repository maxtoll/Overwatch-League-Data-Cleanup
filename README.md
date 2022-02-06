# Overwatch-League-Data-Cleanup
Repository of code I used to clean and organize data from the Overwatch League using SQL (specifically SQLite).

The original source of the raw data can be found here: https://overwatchleague.com/en-us/statslab

## Before
![Overwatch League Data raw](https://user-images.githubusercontent.com/97869630/152226888-bdc4aa8b-30c1-4126-bbae-a083f2b9c8ba.PNG)
- 14 CSV files
- Spelling errors
- Inconsistent formatting
- Missing values
- Duplicate rows

## After
![Overwatch League Database organized](https://user-images.githubusercontent.com/97869630/152306351-3733b08d-6449-48ed-9d1a-a62543a7ee78.PNG)

## What I Learned
- https://liquipedia.net/overwatch/ was a great resource in helping understand and validate certain parts of the data
- Database normalization and the normal forms
- Sargable queries
- Expressions to help troubleshoot the dataset: 
  -  IS / IS NOT NULL
  -  DISTINCT
  -  COUNT(column) <> COUNT(DISTINCT(column))

## Plans for Improvement
- Determine a good primary key for player_stat
- Study more set theory

