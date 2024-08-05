# 리스트 3개 중첩 후 입력한 수에 해당하는 인덱스 값 X 로 바꾸기
# 가로 기준 A B C

# 1. 리스트 생성하기
#          A     B    C
line_1 = ["∎", "∎", "∎"] # 1 
line_2 = ["∎", "∎", "∎"] # 2
line_3 = ["∎", "∎", "∎"] # 3
map = [line_1, line_2, line_3]

print("Hiding your treasure! X mark the map") # 첫 출력 문구

# 2. X로 바꿀 값 입력 받기
position = input("Where do you put the treasure? ") # 입력받기

width_str= position[0].upper() # 대문자 고정
width_list = ["A", "B", "C"] # 가로 위치 

width = width_list.index(width_str) # 가로 인덱스 번호 찾기 (A = 0 ...)
height = int(position[1]) - 1 # 세로 인덱스 (1 -> 0 ...)

map[height][width] = "X" # 변환

print(f"{line_1}\n{line_2}\n{line_3}") # 줄바꿈 출력