# 학생들의 점수 중 가장 높은 점수 구하기 (max 함수 직접 구현)

# 1. 입력 받기
stydent_score = input().split() # map(int.input().split())

score_list = []
for i in stydent_score :
    score_list.append(int(i))

# 2. 최고점수 구하기
max_score = 0

for score in score_list:
    if score > max_score: # for문 반복으로 최고값 업데이트
        max_score = score

# 3. 출력
print(f"the hights score in the class is: {max_score}")

