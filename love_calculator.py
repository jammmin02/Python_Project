print("The love calculator is calculating your score...")

Name1 = input("What is your name? ")
Name2 = input("What is their name? ")

# 대문자 소문자 통일 위해서
Name1 = Name1.lower() 
Name2 = Name2.lower() 

# 1 . true　몇 번 나오는지 확인하기

true_count = 0

for i in Name1:
    if i == "t" or i == "r" or i == "u" or i == "e" :
        true_count += 1

for i in Name2:
    if i == "t" or i == "r" or i == "u" or i == "e" :
        true_count += 1

love_count = 0
    
for i in Name1:
    if i == "l" or i == "o" or i == "v" or i == "e" :
        love_count += 1

for i in Name2:
    if i == "l" or i == "o" or i == "v" or i == "e" :
        love_count += 1

score_count = str(true_count) + str(love_count)

