# 주어진 벽의 높이와 너비를 바탕으로 벽면을 칠하는데 필요한 페인트 통 개수 구하기
# 올림 필수
import math

# 2. 면적 구하기
def paint_calc(height, widht, cover):
    number_of_cans =(height * widht) / cover
    round_up_can = math.ceil(number_of_cans)
    print(f"your'll need {round_up_can} cans of paint.")
    
# 1. 높이 너비 입력받기
teat_h = int(input("height of wall(m): "))
teat_w = int(input("width of wall(m): "))
coverage = 5

# 3. 함수 호출
paint_calc(teat_h, teat_w, coverage)


