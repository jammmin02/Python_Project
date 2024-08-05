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
position = input("Where do you put the treasure? ")

width = ord(position[0].upper()) # 아스키 코드 변환
height = int(position[1]) # 정수화

widht_list = [65, 66, 67] # 아스키 코드 (A, B, C)
height_list = [1, 2, 3]

# 3. 바꾸기 
for i in widht_list : # 가로 반복
    for y in height_list: # 세로 반복
        if width == i and height == y: # 가로 세로 값이 모두 같다면
            map[height_list.index(y)][widht_list.index(i)] = "X" # 변경

# 4. 출력
for i in map : # 리스트 출력
    print(i)

