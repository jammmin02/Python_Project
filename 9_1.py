# 학생들의 시험 점수에 성적 매기기
# 점수 딕셔너리에서 내용을 가지고 온 후 각 학생의 점수를 성적으로 변환
# 성적에 대한 딕셔너리 생성

# 1. 점수 딕셔너리 생성
student_scores = {
    "jumg" : 81,
    "min" : 78,
    "heri" : 99,
    "kara" : 74,
    "neville" : 62,
}

# 2. 빈 성적 딕셔너리 생성
student_grades = {} 

# 3. 조건에 딕셔너리 생성
for score in student_scores:
    grades = student_scores[score]
    if grades > 90 and grades <= 100:
        student_grades[score] = "매우 우수"
    elif grades > 80 and grades <= 90:
        student_grades[score] = "우수"
    elif grades > 70 and grades <= 80:
        student_grades[score] = "보통"
    else :
        student_grades[score] = "부족"

print(student_grades) # 출력