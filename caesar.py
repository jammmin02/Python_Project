# 카이샤르 암호화 하기
# 입력받은 문자를 입력한 숫자만큼 인덱스 옮겨서 출력하기
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# 암호화 함수
def encrpt(plain_text, shift_amount):
    text_list = [i for i in plain_text]
    for i in text_list:
        position = alphabet.index(i) + shift_amount
        if position > 25 :
            position_over = position - 26
            print(alphabet[position_over],end="")
        else: 
            print(alphabet[position],end="")

# 복호화
def decrpt(cipher_text, plain_amount):
    text_list = [i for i in  cipher_text]
    for i in text_list:
        position = alphabet.index(i) - plain_amount
        if position < 0 :
            position_over = position + 26
            print(alphabet[position_over],end="")
        else: 
            print(alphabet[position],end="")

def caesar(direct, start_text, shift_amount):
    text_list = [i for i in  start_text]
    for i in text_list:
        position = alphabet.index(i) + shift_amount
        if direct == "decode":
            position *= - 1
        if position > 25 :
            position_over = position - 26
            print(alphabet[position_over],end="")
        elif position < 0 :
            position_over = position + 26
            print(alphabet[position_over],end="")
        else: 
            print(alphabet[position],end="")
        

# 1. 문자열과 수 입력받기
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower() # 문자열 입력
shift = int(input("Type the shift number:\n")) # 옮길 수 입력

if direction == "encode":
    encrpt(text, shift)

elif direction == "decode":
    decrpt(text, shift)
