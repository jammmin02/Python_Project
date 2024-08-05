# 소수인지 아닌지 판별 (자기자신과 1외에는 나눠지지 않는 수)

# 2. 소수인지 판별하는 함수
def prime_checker(number):
    is_prime = True
    for num in range (2, number):
        if number % num == 0 :
            is_prime = False
    if is_prime :
        print("it's a prime number")
    else :
        print("it's a not prime number")
        
# 1. 숫자 입력받기
checker_num = int(input("Check this number: "))

# 3. 함수 호출
prime_checker(checker_num)

