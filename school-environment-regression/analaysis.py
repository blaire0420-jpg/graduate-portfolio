import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# 1. 학교 환경 데이터 만들기
data = {
    "study_hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "average_score": [52, 55, 61, 65, 70, 74, 80, 85]
}

df = pd.DataFrame(data)

# 2. 독립변수와 종속변수 설정
X = df[["study_hours"]]
y = df["average_score"]

# 3. 선형회귀 모델 학습
model = LinearRegression()
model.fit(X, y)

# 4. 예측값 계산
df["predicted_score"] = model.predict(X)

# 5. 회귀분석 결과 출력
print("=== Regression Analysis ===")
print(f"Regression coefficient: {model.coef_[0]:.2f}")
print(f"Intercept: {model.intercept_:.2f}")
print(f"R-squared: {model.score(X, y):.4f}")
print("\n=== Actual vs Predicted ===")
print(df.round(2))

# 6. 산점도와 회귀선 시각화
plt.scatter(df["study_hours"], y, label="Actual scores")
plt.plot(
    df["study_hours"],
    df["predicted_score"],
    label="Regression line"
)

plt.xlabel("Study Hours")
plt.ylabel("Average Score")
plt.title("Study Hours and Academic Performance")
plt.legend()
plt.tight_layout()

# 7. 그래프 저장
plt.savefig("regression_analysis.png")
plt.show()
