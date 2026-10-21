import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
# 학생 성적 데이터 생성 (연습용 가상 데이터)
data = {
    "study_hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "attendance": [60, 65, 70, 75, 80, 85, 90, 92, 95, 98],
    "assignment_score": [50, 55, 60, 65, 70, 75, 80, 85, 90, 95],
    "exam_score": [45, 50, 55, 60, 65, 70, 75, 80, 85, 95]
}

df = pd.DataFrame(data)

print("Student Performance Dataset")
print(df)

df.to_csv("student_scores.csv", index=False)

print("CSV file saved successfully!")


# Basic statistical analysis
print("\nBasic Statistics")
print(df.describe())

print("\nAverage Exam Score:", df["exam_score"].mean())
print("Highest Exam Score:", df["exam_score"].max())
print("Lowest Exam Score:", df["exam_score"].min())

# Correlation analysis
print("\nCorrelation Analysis")
print(df.corr())


import matplotlib.pyplot as plt

# Study hours vs exam scores
plt.figure(figsize=(8, 5))

plt.scatter(
    df["study_hours"],
    df["exam_score"],
    color="blue"
)

plt.title("Study Hours vs Exam Scores")
plt.xlabel("Study Hours")
plt.ylabel("Exam Scores")
plt.grid(True)

plt.savefig("study_hours_vs_scores.png")
plt.show()

# 1. 학습 데이터 준비
X = df[["study_hours"]]
y = df["exam_score"]

# 2. 머신러닝 모델 생성
model = LinearRegression()

# 3. 데이터 학습
# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train the model
model.fit(X_train, y_train)

# Predict scores for unseen test data
predicted_scores = model.predict(X_test)

# Evaluate the model
mae = mean_absolute_error(y_test, predicted_scores)
r2 = r2_score(y_test, predicted_scores)

# 4. 하루 7.5시간 공부했을 때 점수 예측
new_data = pd.DataFrame({"study_hours": [7.5]})
prediction = model.predict(new_data)

print("\nMachine Learning Prediction")
print(f"Predicted Exam Score: {prediction[0]:.2f}")

# 5. 학습한 직선의 기울기와 절편
print("Coefficient:", model.coef_[0])
print("Intercept:", model.intercept_)

# Visualize machine learning predictions
plt.figure(figsize=(8, 5))

# Actual exam scores
plt.scatter(
    X["study_hours"],
    y,
    color="blue",
    label="Actual Scores"
)

# Predicted scores
predicted_scores = model.predict(X)

plt.plot(
    X["study_hours"],
    predicted_scores,
    color="red",
    label="Predicted Scores"
)

# Predict 7.5 study hours
plt.scatter(
    7.5,
    prediction[0],
    color="green",
    s=120,
    label="7.5 Hours Prediction"
)

plt.title("Student Score Prediction")
plt.xlabel("Study Hours")
plt.ylabel("Exam Score")
plt.legend()
plt.grid(True)

plt.savefig("machine_learning_prediction.png")
plt.show()

from sklearn.metrics import mean_absolute_error, r2_score


# Model evaluation on unseen test data
predicted_scores = model.predict(X_test)

mae = mean_absolute_error(y_test, predicted_scores)
r2 = r2_score(y_test, predicted_scores)

print("\nTest Set Evaluation")
print(f"Mean Absolute Error (MAE): {mae:.2f}")
print(f"R-squared (R2): {r2:.4f}")

# Compare actual and predicted scores on the test set
plt.figure(figsize=(8, 6))

plt.scatter(y_test, predicted_scores)

plt.plot(
    [min(y_test), max(y_test)],
    [min(y_test), max(y_test)],
    color="red",
    linestyle="--"
)

plt.xlabel("Actual Scores")
plt.ylabel("Predicted Scores")
plt.title("Actual vs Predicted Scores (Test Set)")
plt.grid(True)

plt.savefig("actual_vs_predicted.png")
plt.show()
