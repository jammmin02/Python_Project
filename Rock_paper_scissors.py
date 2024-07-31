# 가위바위보 게임 
# 유저는 0, 1, 2 를 입력하여 각각 바위 = 0 보 = 1 가위 = 2
# 입력 하면 유저 그래픽 생성, 컴퓨터 그래픽 생성
import random

# 1. 그래픽 출력
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# 2. 유저 입력 받기
RPS= [rock, paper, scissors] # 가위바위보 관리 리스트 생성
user = int(input("0 ~ 2 중에 선택하세요 (바위 = 0 보 = 1 가위 = 2): "))
print(RPS[user]) # 2-1. 유저 입력 출력

# 3. 컴퓨터 입력 받기
com_num = random.randint(0,2)
print(f"computer :\n{RPS[com_num]}") # 3-1. 컴퓨터 랜덤값 출력

#4. 결과 출력하기
if user == com_num :
    print("비겼습니다")
elif user == 0 and com_num == 2 or user == 1 and com_num == 0 or user == 2 and com_num == 1 :
    print("당신이 이겼습니다")
else :
    print("당신이 졌습니다")
