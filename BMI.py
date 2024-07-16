height = input() # 키
weight = input() # 몸무게

bmi_height=float(height) # 실수 변환
bmi_weight=int(weight) # 정수 변환

bmi = (bmi_weight//(bmi_height**2)) # bmi 계산

print(int(bmi)) # 정수로 출력