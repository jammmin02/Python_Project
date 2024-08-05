# 학생들 키의 합계, 인원수, 평균 구하기

# 1. 입력 받기
student_heights = input().split() 

# 2. 합계 인원수 평균 구하기
student_sum = 0 # 합계
student_len = 0 # 학생 수

for i in student_heights : # 반복
    student_sum += int(i) # 합계
    student_len += 1 # 학생 수

# 3. 출력
print(f"total heights = {student_sum}")
print(f"number of student = {student_len}")
print(f"average height = {round(student_sum/student_len)}")

    
