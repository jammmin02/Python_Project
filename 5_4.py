# fizzbuzz 게임 구현하기 (1~100까지 출력)
# 3으로 나눠지면 fizz 5로 나눠지면 buzz 둘다 나눠지면 fizzbuzz

# 반복문으로 구현하기
for num in range(1, 101):
    if num % 15 == 0: # num % 3 == 0 and num % 5 == 0
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else :
        print(num)