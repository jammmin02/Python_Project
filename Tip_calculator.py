print("Welcom to the tip calculator.") # 안내 메세지

bill = float(input("What was the total bill? $")) # 영수증 금액
tip_persente= int(input("?")) # 팁 퍼센트
num = int(input("?")) # 인원수

tip_bill = bill + (bill * (tip_persente / 100)) # 팁을 포함한 영수증 금액
total_bill = round((tip_bill / num) , 2 ) # tip_bill에서 인원수 만큼 나눈 금액 (소수 둘째자리까지)

print(total_bill) # 출력ㄴ

