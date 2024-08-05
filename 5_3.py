# 입력된 숫자내에 짝수의 합 구하기 0 < input()

# 1. 입력받기
target = int(input("Number between 0 and 1000: "))

# 2. 짝수의 합 구하기
even_sum = 0

for num in range(0,target + 1):
    if num % 2 == 0:  # 짝수라면
        even_sum += num # 더하기
# for num in range(0, target + 1, 2):
#   even_sum += num

# 3. 출력하기
print(f"sum : {even_sum}")