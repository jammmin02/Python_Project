alphabet = 'abcdefghijklmnopqrstuvwxyz'

# 암호화 및 복호화 함수
def caesar_cipher(text, shift, mode='encode'):
    shift = shift if mode == 'encode' else -shift
    result = ''
    for char in text:
        if char in alphabet:
            position = (alphabet.index(char) + shift) % 26
            result += alphabet[position]
        # else:
        #     result += char
    return result

# 1. 문자열과 수 입력받기
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower() # 문자열 입력
shift = int(input("Type the shift number:\n")) # 옮길 수 입력

# 결과 출력
print(caesar_cipher(text, shift, direction))