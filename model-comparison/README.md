# Machine Learning Model Comparison

## Project Overview
This project compares Linear Regression and Random Forest models for predicting student final scores.

## Dataset
- 20 sample student records
- Features: study hours, attendance rate, previous score
- Target: final score
- Note: This is a simulated educational dataset for practice, not real student data.

## Models
- Linear Regression
- Random Forest Regressor

## Evaluation Metrics
- MAE (Mean Absolute Error): lower is better
- RMSE (Root Mean Squared Error): lower is better
- R² (Coefficient of Determination): closer to 1 is generally better

## Results
| Model | MAE | RMSE | R² |
|---|---:|---:|---:|
| Linear Regression | 0.75 | 1.03 | 1.00 |
| Random Forest | 1.47 | 1.68 | 0.99 |

Linear Regression performed better on this particular test split. Because the dataset is small and simulated, these results should not be generalized to real-world student outcomes.

## Files
- `model_comparison.py`: trains and evaluates both models
- `model_comparison_results.csv`: saved model evaluation results

## How to Run
```bash
python model-comparison/model_comparison.py