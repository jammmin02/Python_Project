# 리스트안에서 단어하나를 고르고 단어 맞추기 다 맞출때까지 끝나지 않음
# 일정이상 반복횟수 초과시 게임 종료

import random
word = ["ardvark", "baboon", "camel"]

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


# 1. 리스트 내에서 단어 고르기
com_word = random.choice(word)
# 1-1. 선택된 글자의 수만큼 "-"표시하기
display = ["_"] * len(com_word)
word_list = [i for i in com_word]

for i in display:
    print(i, end=" ")
print()

end_game = False
stages_life = 6

# 2. 단어 입력받기
# 3. 철자가 단어안에 있는지 확인하기
while not end_game: # 게임이 종료될 때 까지
    user = input("철자를 입력하세요: ").lower() # 대소문자 통합
    
    for word in word_list: # user가 올바른 단어를 선택했는가
        if word == user : 
            letter = word_list.index(word) # 인덱스번호 추출
            display[letter] = user # "_" 변경
            word_list[letter] = "*" # 중복체크 방지
    
    if user not in word_list:
        stages_life -= 1
        if stages_life == 0:
            end_game = True
            print("Your lose")

    for i in display: # 디스플레이 출력(맞춘단어가 있다면 변경 후 출력)
        print(i, end=" ")
    print()

    # if user not in word_list:
    #     print(stages[stages_life])
    #     stages_life -= 1
    #     if stages_life == 0:
    #         end_game = True
    #         print("Your lose")

    if "_" not in display: # 단어를 모두 맞추면 게임 종료
        print("Your Win")
        end_game = True

