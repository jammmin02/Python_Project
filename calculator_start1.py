def add(num1, num2): # 더하기
    return num1 + num2

def subtract(num1, num2): # 빼기
    return num1 - num2

def multiply(num1, num2): # 곱하기
    return num1 * num2

def divide(num1, num2): # 나누기
    return num1 / num2

opreations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}
while True:
    if type == "n":
        print("계산기를 종료합니다")
        break

    first_num = float(input("첫번째 숫자를 입력하세요: "))
    
    while True:
        for symbol in opreations: # 연산자 출력하기
            print(symbol)

        opreations_symbol = input("연산자를 고르세요: ") # 연산자 선택

        next_num = float(input("계산 할 숫자를 입력하세요: ")) # 첫번째 숫자 선택

        Calculator_function = opreations[opreations_symbol] # 딕셔너리 키값 불러오ㄱ;
        # 정답 출력
        answer = Calculator_function(first_num, next_num)

        print(f"{first_num} {opreations_symbol} {next_num} = {answer}")
        
        # 게임 진행 여부 판단
        type = input(f"type 'y' 선택시 {answer}에 이어서 계산 진행, type 's' 선택시 새로 진행 ,type 'n' 선택시 종료: ").lower()
        
        if type == "y" :
            first_num = answer
            
        elif type =="n" or type == "s" :
            break