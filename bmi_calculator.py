height = float(input("키를 입력하세요: "))
weight = int(input("몸무게를 입력하세요: "))

bmi = (weight/(height**2))

if bmi < 18.5 :
    print("저체중 입니다")
elif bmi >= 18.5 and bmi < 25 :
    print("정상체중 입니다")
elif bmi >= 25 and bmi < 30 :
    print("경도비만 입니다") : 
elif bmi >= 30 and bmi < 35 :
    print("중등도비만 입니다")
else :
    print("초고도비만 입니다")