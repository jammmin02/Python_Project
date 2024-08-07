programming_dictionary = {
    "a"  : "apple",
    "b"  : "banana",
    "c" : "cat",
}

programming_dictionary["a"] = "app" # 키 내용 변경

empty_dictionary = {} 

# programming_dictionary = {} # 딕셔너리 초기화
#print(programming_dictionary) # 빈 딕셔너리 출력

programming_dictionary["d"] = "day"

# 루프를 활용한 딕셔너리

for key in programming_dictionary:
    #print(key)
    print(programming_dictionary[key])