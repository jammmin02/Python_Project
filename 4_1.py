import random

names = input("이름을 입력하세요: ").split() # 문자열 분리

names_len = len(names) # 길이 

names_choic = random.randint(0, names_len - 1) # 선택(인덱스번호)

print(f"선택된 사람은 {names[names_choic]} 입니다") # 출력