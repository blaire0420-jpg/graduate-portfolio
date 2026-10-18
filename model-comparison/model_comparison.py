import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

# Create a sample student dataset
data = {
    "study_hours": [1, 2, 3, 4, 5, 6, 7, 8, 2, 5, 6, 9, 3, 7, 4, 8, 1, 9, 6, 10],
    "attendance": [60, 65, 70, 75, 80, 85, 90, 95, 68, 82, 86, 98, 72, 91, 78, 96, 62, 99, 88, 100],
    "previous_score": [50, 55, 60, 62, 70, 72, 80, 85, 58, 68, 75, 90, 61, 79, 66, 88, 48, 92, 77, 95],
    "final_score": [52, 57, 63, 65, 73, 75, 82, 88, 59, 71, 78, 93, 64, 81, 69, 91, 50, 95, 80, 98]
}

df = pd.DataFrame(data)
X = df[["study_hours", "attendance", "previous_score"]]
y = df["final_score"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

models = {
    "Linear Regression": LinearRegression(),
    "Random Forest": RandomForestRegressor(n_estimators=100, random_state=42)
}

results = []

for name, model in models.items():
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    results.append({
        "Model": name,
        "MAE": round(mean_absolute_error(y_test, predictions), 2),
        "RMSE": round(np.sqrt(mean_squared_error(y_test, predictions)), 2),
        "R2": round(r2_score(y_test, predictions), 2)
    })

results_df = pd.DataFrame(results)
print("Model Comparison Results")
print(results_df.to_string(index=False))
results_df.to_csv("model_comparison_results.csv", index=False)
print("\nResults saved to model_comparison_results.csv")
