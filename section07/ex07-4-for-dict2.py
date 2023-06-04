students = [
    {"이름":"John", "국어":90, "영어":85, "수학":95},
    {"이름":"Emily", "국어":92, "영어":88, "수학":96},
    {"이름":"Michael", "국어":98, "영어":90, "수학":92},
    {"이름":"Jessica", "국어":88, "영어":82, "수학":78}
]

#테이블 헤더 출력
print("이름\t국어\t영어\t수학")
print("=====================")

#각학생의 성적 출력
for student in students:
    name = student["이름"]
    korean = student["국어"]
    english = student["영어"]
    math = student["수학"]
    print(f"{name}\t{korean}\t{english}\t{math}")