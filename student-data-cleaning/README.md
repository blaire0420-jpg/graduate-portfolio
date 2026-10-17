# Student Data Cleaning and ML Evaluation

## Project Overview
This project demonstrates data cleaning and machine learning evaluation using Python.

## Tools
- Python
- pandas
- scikit-learn

## Data Cleaning
- Identified missing values
- Filled missing values using column means
- Removed duplicate rows
- Exported cleaned data to CSV

## Machine Learning
- Used study hours and attendance to predict student scores
- Split data into training and testing sets
- Trained a Linear Regression model

## Evaluation Results
- MAE: 5.48
- RMSE: 6.44
- R² Score: 0.87

## Files
- `analysis.py`: Data cleaning and model evaluation code
- `cleaned_student_data.csv`: Cleaned dataset
- `prediction_results.csv`: Actual and predicted scores

## Limitations
The dataset contains only 10 simulated observations. The evaluation results are for learning purposes and should not be generalized to real students.

## Future Improvements
- Use a larger real-world dataset
- Apply cross-validation
- Compare multiple machine learning models
