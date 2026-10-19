import pandas as pd
from pathlib import Path

# 1. 연습용 학생 데이터 만들기
data = {
    "study_hours": [2, 3, 4, None, 6, 7, 3, 5, 5, 8],
    "attendance": [60, 70, 80, 75, None, 95, 70, 85, 85, 100],
    "score": [50, 55, 65, 60, 75, 90, 55, 70, 70, 95]
}

df = pd.DataFrame(data)



print("\n=== Data Cleaning Report ===")
print(f"Original rows: {len(df)}")
print(f"Missing values before cleaning: {df.isnull().sum().sum()}")
print("=== Original Data ===")
print(df)

# 2. 결측치 확인
print("\n=== Missing Values ===")
print(df.isnull().sum())

# 3. 결측치를 각 열의 평균으로 채우기
df["study_hours"] = df["study_hours"].fillna(
    df["study_hours"].mean()
)
df["attendance"] = df["attendance"].fillna(
    df["attendance"].mean()
)

# 4. 중복 행 제거
rows_before = len(df)
df = df.drop_duplicates()
rows_after = len(df)

print("\n=== Duplicate Removal Report ===")
print(f"Rows before removing duplicates: {rows_before}")
print(f"Rows after removing duplicates: {rows_after}")
print(f"Duplicate rows removed: {rows_before - rows_after}")

# 5. 정리된 데이터 확인
print("\n=== Cleaned Data ===")
print(df)

print("\n=== Summary Statistics ===")
print(df.describe())

# 6. 결과 저장
output_path = Path(__file__).parent / "cleaned_student_data.csv"
df.to_csv(output_path, index=False)

print(f"\nCleaned data saved to: {output_path}")


# 7. 머신러닝 모델 학습 및 평가
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

# 입력 변수와 예측할 변수 분리
X = df[["study_hours", "attendance"]]
y = df["score"]

# 학습 데이터와 테스트 데이터 분리
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# 선형회귀 모델 학습
model = LinearRegression()
model.fit(X_train, y_train)

# 테스트 데이터로 예측
y_pred = model.predict(X_test)

# 모델 성능 평가
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print("\n=== Model Evaluation ===")
print(f"MAE: {mae:.2f}")
print(f"RMSE: {rmse:.2f}")
print(f"R² Score: {r2:.2f}")

# 실제 점수와 예측 점수 비교
results = pd.DataFrame({
    "Actual Score": y_test.values,
    "Predicted Score": y_pred.round(2)
})

print("\n=== Actual vs Predicted ===")
print(results)

results.to_csv(
    Path(__file__).parent / "prediction_results.csv",
    index=False
)

print("\nPrediction results saved successfully!")
