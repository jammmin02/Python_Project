#년도 입력받기
year = int(input("년도를 입력하세요: "))
# 1. 4로 나눴을때 나머지가 0
if year % 4 == 0:
    if year % 100 != 0: # 2. 4로 나눴을때 0 100으로 나눴을때 0이 아니면 윤년
        print("윤년입니다")
    else :
        if year % 400 == 0 : # 3. 만약 100으로 나눴을 때 나머지가 0이 아니라면
            print("윤년입니다") # 400으로 나눴을 때 0이면 윤년
        else :
            print("윤년이 아닙니다") # 아니면 윤년 아님 
else :
    print("윤년이 아닙니다") # 4로 나눴을때 나머지가 있다면 윤년 아님