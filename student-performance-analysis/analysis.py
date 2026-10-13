import pandas as pd
import matplotlib.pyplot as plt

# 한글 폰트 설정
plt.rcParams["font.family"] = "AppleGothic"
plt.rcParams["axes.unicode_minus"] = False

# 1. 데이터 불러오기
students = pd.read_excel("students.xlsx")

# 2. 열 이름 정리
students.columns = (
    students.columns
    .str.replace("\n", "", regex=False)
    .str.replace(" ", "", regex=False)
)

# 3. 분석에 사용할 변수를 숫자로 변환
students["수업교원1인당학생수"] = pd.to_numeric(
    students["수업교원1인당학생수"],
    errors="coerce"
)

students["학급당학생수"] = pd.to_numeric(
    students["계.2"],
    errors="coerce"
)

# 시군 추출
students["시군"] = students["지역"].str.split().str[1]

# 4. 시군별 교원 1인당 학생 수
teacher_by_city = (
    students.groupby("시군")["수업교원1인당학생수"]
    .mean()
    .sort_values()
)

print("시군별 교원 1인당 학생 수")
print(teacher_by_city)

plt.figure(figsize=(10, 8))
teacher_by_city.plot(kind="barh")
plt.title("경기도 시군별 교원 1인당 학생 수")
plt.xlabel("교원 1인당 학생 수")
plt.ylabel("시군")
plt.tight_layout()
plt.savefig("city_comparison.png", dpi=300)
plt.close()

# 5. 공립·사립 비교
school_type_avg = (
    students.groupby("설립구분")["수업교원1인당학생수"]
    .mean()
    .dropna()
)

print("\n설립구분별 교원 1인당 학생 수")
print(school_type_avg)

school_type_avg.plot(kind="bar")
plt.title("설립구분별 교원 1인당 학생 수")
plt.xlabel("설립구분")
plt.ylabel("교원 1인당 학생 수")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("school_type_comparison.png", dpi=300)
plt.close()

# 6. 시군별 학급당 학생 수
class_size_by_city = (
    students.groupby("시군")["학급당학생수"]
    .mean()
    .sort_values()
)

print("\n시군별 학급당 학생 수")
print(class_size_by_city)

plt.figure(figsize=(10, 8))
class_size_by_city.plot(kind="barh")
plt.title("경기도 시군별 학급당 학생 수")
plt.xlabel("학급당 학생 수")
plt.ylabel("시군")
plt.tight_layout()
plt.savefig("class_size_by_city.png", dpi=300)
plt.close()

# 7. 상관관계 분석
correlation = students[
    ["학급당학생수", "수업교원1인당학생수"]
].corr()

print("\n상관관계")
print(correlation)

# 8. 산점도
plt.figure(figsize=(8, 6))
plt.scatter(
    students["학급당학생수"],
    students["수업교원1인당학생수"]
)

plt.title("학급당 학생 수와 교원 1인당 학생 수의 관계")
plt.xlabel("학급당 학생 수")
plt.ylabel("교원 1인당 학생 수")
plt.tight_layout()
plt.savefig("class_size_vs_teacher_ratio.png", dpi=300)
plt.close()