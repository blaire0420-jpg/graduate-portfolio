# Educational Environment Analysis of High Schools in Gyeonggi-do

## Project Overview

This project analyzes the educational environment of high schools in Gyeonggi-do, South Korea, using publicly available school data.

The main goal is to examine regional differences in school educational environments using indicators such as class size and the number of students per teacher.

## Data Source

- School Information Disclosure System (학교알리미)
- Region: Gyeonggi-do
- School level: High School
- Year: 2026

## Research Questions

1. How does the number of students per teacher differ across regions?
2. How does average class size differ across regions?
3. Is there a difference between public and private high schools?
4. Is class size related to the number of students per teacher?

## Tools

- Python
- pandas
- matplotlib

## Analysis

The analysis includes:

- Data cleaning and preprocessing
- Regional comparison of students per teacher
- Comparison between public and private schools
- Regional comparison of average class size
- Correlation analysis between class size and students per teacher
- Data visualization

## Key Findings

- Considerable regional variation was observed in class size and students per teacher.
- Hwaseong-si showed the highest average class size among the analyzed regions.
- The difference in students per teacher between public and private schools was small.
- Class size and students per teacher showed a strong positive correlation (r ≈ 0.96).

## Interpretation

Schools with larger classes tended to have more students per teacher. However, these two indicators are structurally related, so the correlation should not be interpreted as a causal relationship.

The results suggest that educational environment indicators can vary substantially across regions within Gyeonggi-do.

## Limitations

This analysis focuses on school environment indicators and does not directly measure student academic achievement.

Factors such as school size, school type, local population, and socioeconomic characteristics may also influence regional differences.

Therefore, the results should be interpreted as descriptive patterns rather than causal effects.

## Visualizations

### Students per Teacher by City

![Students per Teacher by City](city_comparison.png)

### Class Size by City

![Class Size by City](class_size_by_city.png)

### Class Size vs Students per Teacher

![Class Size vs Students per Teacher](class_size_vs_teacher_ratio.png)

### Public vs Private Schools

![Public vs Private Schools](school_type_comparison.png)