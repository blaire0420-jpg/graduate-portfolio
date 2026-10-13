import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "AppleGothic"
plt.rcParams["axes.unicode_minus"] = False
students = pd.read_excel("students.xlsx")

print(students.head())
print(students.columns.tolist())
students.columns = students.columns.str.replace("\n", "").str.replace(" ", "")
print(students.columns.tolist())

students["수업교원1인당학생수"] = pd.to_numeric(
    students["수업교원1인당학생수"],
    errors="coerce"
)

print(students["수업교원1인당학생수"].describe())

region_avg = students.groupby("지역")["수업교원1인당학생수"].mean()

print(region_avg.sort_values())

school_type_avg = students.groupby("설립구분")["수업교원1인당학생수"].mean()

print(school_type_avg)
school_type_avg = school_type_avg.dropna()

school_type_avg.plot(
    kind="bar",
    xticks=[0, 1]
)

plt.xticks([0, 1], ["Public", "Private"], rotation=0)

plt.title("Students per Teacher by School Type")
plt.xlabel("School Type")
plt.ylabel("Students per Teacher")
plt.tight_layout()
plt.savefig("school_type_comparison.png", dpi=300)
plt.figure(figsize=(10, 8))

region_avg.sort_values().plot(kind="barh")

plt.title("Students per Teacher by Region")
plt.xlabel("Students per Teacher")
plt.ylabel("Region")
plt.tight_layout()
plt.savefig("region_comparison.png", dpi=300)

# 지역별 교원 1인당 학생 수
region_avg = region_avg.dropna().sort_values()

region_avg.plot(kind="bar", figsize=(12, 6))

plt.title("Students per Teacher by Region")
plt.xlabel("Region")
plt.ylabel("Students per Teacher")
plt.tight_layout()

plt.savefig("region_comparison.png", dpi=300)
students["시군"] = students["지역"].str.split().str[1]

city_avg = students.groupby("시군")["수업교원1인당학생수"].mean()
city_avg = city_avg.sort_values()

print(city_avg)
plt.figure(figsize=(10, 8))

city_avg.plot(kind="barh")

plt.title("경기도 시군별 수업 교원 1인당 학생 수")
plt.xlabel("수업 교원 1인당 학생 수")
plt.ylabel("시군")
plt.tight_layout()

plt.savefig("city_comparison.png", dpi=300)

print("학생 수가 가장 적은 5개 시군")
print(city_avg.head(5))

print("학생 수가 가장 많은 5개 시군")
print(city_avg.tail(5))
print("교원 1인당 학생 수가 가장 적은 5개 시군")
print(city_avg.head(5))

print("교원 1인당 학생 수가 가장 많은 5개 시군")
print(city_avg.tail(5))
print(students[["학교명", "계", "계.1", "계.2"]].head(10))
students["학급당학생수"] = pd.to_numeric(students["계.2"], errors="coerce")

class_size_by_city = students.groupby("시군")["학급당학생수"].mean()
class_size_by_city = class_size_by_city.sort_values()

print(class_size_by_city)
correlation = students[
    ["학급당학생수", "수업교원1인당학생수"]
].corr()

print(correlation)
plt.figure(figsize=(8, 6))

plt.scatter(
    students["학급당학생수"],
    students["수업교원1인당학생수"]
)

plt.title("Class Size vs Students per Teacher")
plt.xlabel("Average Students per Class")
plt.ylabel("Students per Teacher")
plt.tight_layout()

plt.savefig("class_size_vs_teacher_ratio.png", dpi=300)
plt.close()
teachers = pd.read_excel("teachers.xlsx")
schools = pd.read_excel("schools.xlsx")

print("교원 데이터")
print(teachers.columns.tolist())

print("학교 기본정보")
print(schools.columns.tolist())
print(teachers.columns.tolist()[:20])