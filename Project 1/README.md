# Project 1: Indeed Data Analysis

## Overview

In this portfolio entry, I showcase a recent project where I utilized data from Indeed to create insightful visualizations displaying the prevalence of specific skills and certifications across various job roles.

## Contents

- [Code](./code)
  - [Code used to clean](./code/cleaned_file_code.py)
  - [Fuzzywuzzy matching code](./code/fuzzywuzzy_indeed_matching.py)
- [Data](./data)
  - [Cleaned Data](./data/cleaned_data.csv)
  - [Final Certifications and Skills](./data/final_certifications_skills.csv)
- [Dashboard](./dashboard)
  - [Dashboard](./images/Indeed_Analysis_Dashboard.png)


## Project Description

In this portfolio entry, I present a captivating exploration into the landscape of job skills and certifications through an innovative analysis of data harvested from Indeed. This project stands as a testament to my prowess in data manipulation, extraction, and visualization, offering a comprehensive view of the skills demanded across diverse job roles.

With meticulous attention to detail, I embarked on a journey to unravel the secrets hidden within 48 job listings each for four distinct positions: "business analyst," "information security analyst," "data analyst," and "systems analyst." The pivotal starting point was data extraction from Indeed's intricate platform, a task laden with unique challenges. To surmount this hurdle, I harnessed the power of the ParseHub program, a robust scraping tool. This endeavor yielded a trove of around 10 distinct files that formed the foundation of my analysis.

The data journey continued with a meticulous cleansing and harmonization process facilitated by the versatile pandas library. Redundant entries were expunged, and each data point underwent a rigorous validation process against predefined benchmarks. The subsequent phase showcased the utilization of the FuzzyWuzzy Python library, a tool for string matching based on similarity ratios. Leveraging this technique, I extracted a comprehensive suite of skills and certifications from the job descriptions. Iterative adjustments to the similarity score threshold were instrumental in striking the ideal equilibrium between efficiency and precision.

Organizing the extracted keywords and certifications into coherent fields laid the groundwork for the creation of captivating visualizations. These visual representations unveiled the most coveted proficiencies within each job category. Notably, a consensus emerged: data documentation stood as the foundational skill across all postings. Furthermore, distinct primary skills surfaced for specific roles, embodying the diverse demands of the job market.

A pivotal visualization was the elucidation of job type distribution through a pie chart, revealing the predilections of companies for contract, full-time, and unspecified positions across different roles. Additionally, certifications associated with each job category were artfully depicted, with a focal point in the realm of Information Security Analyst.

This project served as a learning crucible, endowing me with invaluable insights into the core competencies requisite for success in the realm of data analysis. The challenges faced throughout the journey, from untangling Indeed's data intricacies to optimizing keyword and certification extraction, galvanized the development of effective and innovative solutions.

## Visualizations

![Dashboard](./images/Indeed_Analysis_Dashboard.png)

## Conclusion

In conclusion, the culmination of technical expertise, strategic thinking, and problem-solving acumen birthed a robust analysis that enriched my skill set while unraveling the nuanced dynamics of skill and certification demand in the realm of data analysis. Proficiencies such as SQL, data documentation, data integration, and Excel emerged as cornerstones of success, validated by the comprehensive analysis. This project stands as a testament to my ability to wield data as a powerful tool for insight generation, and the resulting visualizations serve as beacons illuminating the intricacies of the job market's ever-evolving landscape. As I continue to tread the path of data exploration, the experiences and lessons garnered from this undertaking will undoubtedly serve as a compass guiding my journey toward greater analytical prowess and discovery.