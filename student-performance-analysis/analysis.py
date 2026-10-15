
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# 1. 학생 데이터 만들기
data = {
    "study_hours": [1, 2, 3, 4, 5, 6, 7, 8, 2, 5],
    "attendance": [60, 65, 70, 75, 80, 85, 90, 95, 68, 82],
    "sleep_hours": [5, 6, 7, 6, 8, 7, 8, 7, 5, 6],
    "score": [45, 50, 55, 60, 70, 75, 85, 90, 48, 68]
}

df = pd.DataFrame(data)

# 2. 데이터 확인
print("=== Student Data ===")
print(df)

print("\n=== Summary Statistics ===")
print(df.describe())

# 3. 변수 간 상관관계 분석
correlation = df.corr()

print("\n=== Correlation with Score ===")
print(correlation["score"].sort_values(ascending=False))

# 4. 상관관계 히트맵 만들기
plt.figure(figsize=(8, 6))

plt.imshow(correlation, cmap="coolwarm", vmin=-1, vmax=1)
plt.colorbar(label="Correlation")

plt.xticks(range(len(correlation.columns)), correlation.columns, rotation=45)
plt.yticks(range(len(correlation.columns)), correlation.columns)

for i in range(len(correlation.columns)):
    for j in range(len(correlation.columns)):
        plt.text(
            j, i,
            f"{correlation.iloc[i, j]:.2f}",
            ha="center",
            va="center"
        )

plt.title("Student Performance Correlation")
plt.tight_layout()

output_path = Path(__file__).parent / "correlation_heatmap.png"
plt.savefig(output_path, dpi=150)
plt.show()

print(f"\nGraph saved to: {output_path}")
# 5. 분석 결과 저장하기
output_dir = Path(__file__).parent

df.to_csv(
    output_dir / "student_data.csv",
    index=False
)

correlation.to_csv(
    output_dir / "correlation_matrix.csv"
)

print("Data and correlation matrix saved successfully!")
