# Video Game Trend Analysis

## Overview

This analysis dives into video game trends from 1980 to 2023, emphasizing data-driven insights crucial for business decisions in the gaming industry.

## Contents

- [Code](./code)
  - [Data Cleaning](./code/gamesovertime_code.py)
- [Data](./data)
  - [Processed Data](./data/cleaned_gamesovertime.csv)
  - [Original Dataset](./data/gamesovertime_base.csv)
- [Visual Insights](./dashboard)
  - [Analysis Dashboard](./dashboard/gamesovertime.png)

## Project Insights

The dataset provides a comprehensive view of video game trends over four decades. By leveraging data analysis techniques, I've extracted business-critical insights, emphasizing the importance of data in decision-making processes.

## Project Description

This dataset encompasses video games spanning over four decades, featuring key attributes including release dates, user review ratings, and game teams. The dataset was collected from Backloggd, a platform blending gaming collections with social interactions to enhance gaming profiles. A diverse range of statistics is embedded within the dataset.

## Methodology

### Data Extraction

The project began by extracting data from Backloggd, which houses information about games released between 1980 and 2023. Essential fields like 'Release Date', 'User Review Rating', and 'Game Teams' were collected. Data from [Kaggle](https://www.kaggle.com/datasets/arnabchaki/popular-video-games-1980-2023).

### Data Cleaning

A comprehensive data cleaning process was conducted to ensure data readiness for analysis. The code performed the following steps:

- Loaded the original data and maintained consistency in data types.
- Converted 'Release Date' to a datetime format and 'Rating' to a numeric value.
- Processed numeric columns like 'Number of Reviews', 'Plays', 'Playing', 'Backlogs', and 'Wishlist' by converting 'K' values to thousands.
- Dropped the unnecessary 'Times Listed' column.
- Removed rows with missing 'Release Date' values.
- Parsed 'Team' and 'Genres' columns to transform string representations into actual lists.
- Saved the cleaned dataset to a new CSV file for further analysis.

### Visualization

After data cleaning, the dataset was loaded into Excel, and columns like 'Genre' and 'Team' were separated to enhance visualization. Subsequently, Power BI was employed to create a clear and intuitive dashboard. The dashboard focused on:

- Analyzing the distribution of games per genre to identify dominant genres.
- Identifying the highest-rated games and top-performing teams.
- Exploring the average rating of games per year to identify trends.
- Examining game releases per month and the contributions of different companies.

![Dashboard](./dashboard/gamesovertime.png)

## Conclusion

The visualization efforts yielded valuable insights:

- Adventure games dominate the gaming landscape in terms of quantities.
- Notable high-rated games like "Outer Wilds" and "Sekiro: Shadows Die Twice" were identified.
- Prominent companies such as Bay 12 Games and Kitfox Games were highlighted.
- The average rating per year exhibited a downward trend in the past three years.
- Game releases are concentrated towards the end of the year, and Nintendo surpassed other companies in game releases.

This project demonstrates how data analysis and visualization techniques can uncover patterns and trends in the gaming industry over time.

