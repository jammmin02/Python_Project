# 카이샤르 암호화 하기
# 입력받은 문자를 입력한 숫자만큼 인덱스 옮겨서 출력하기
# 진행 중 올바른 문자를 입력한다는 가정

import caesar_art
import string
     
# 암호화 복호화 
def caesar(direct, start_text, shift_amount):
    shift_amount = shift_amount if direct == "encode" else - shift_amount # 복호화 암호화 판단
    result = "" # 출력 할 문자
    for word in start_text: 
        if word in alphabet:
            position  = (alphabet.index(word) + shift_amount) % 26 # 암호화는 26초과시 양수 복호화는 음수
            result += alphabet[position] 
        else :
            result += word # 숫자,공백 유지
            
    print(f"here's your {direct} result: {result}")
               
# 1. 로고 출력 및 알파벳 리스트 생성
loge_art = caesar_art.logo
print(loge_art)
alphabet = [i for i in string.ascii_letters] 

# 게임이 종료될때까지 반복
while True:  
    # 2. 문자열과 수 입력받기
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower() # 문자열 입력  
    while True:
        shift = int(input("Type the shift number:\n")) # 이동 수 입력 (범위 초과하면 다시)
        if shift < len(alphabet):
            break
        else: 
            print("Please input it again(26 > shift)") 

    caesar(direction, text, shift) # 호출
    
    # 게임진행여부 판단
    game = input(" they want to restart the cipher program?(yes or no): ").lower()
    if game == "no" : # 게임을 그만두고 싶다면
        print("Good Bye")
        break
    
   
