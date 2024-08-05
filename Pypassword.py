# 비밀번호 생성기 (중복허용)
# 1. 비밀번호 길이 2. 기호 갯수 3. 문자 갯수
import random
import string

# 리스트 
alp = string.ascii_letters
letters = [i for i in alp]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!") #  첫 메세지 출력

# 1. 비밀번호 생성에 필요한 조건 받기
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# 2 비밀번호 생성하기
passward_list = []
letter_len = (nr_letters-(nr_numbers + nr_symbols))

for _ in range(nr_symbols ):
    passward_list.append(random.choice(symbols))

for _ in range(nr_numbers):
    passward_list.append(random.choice(numbers))

for _ in range(letter_len):
    passward_list.append(random.choice(letters))

random.shuffle(passward_list) # random.shuffle -> 리스트를 무작위로 섞음

# 3. passward 출력
passward = ""
for ward in passward_list:
    passward += ward

print(f"Here is your password: {passward} ")

