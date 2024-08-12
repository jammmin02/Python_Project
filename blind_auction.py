# 비밀경매 프로그램 만들기
# 1. 이름 입력 받기 2. 금액 입력 받기 3. 진행 유무 선택
# 4. 진행 종료 시 가장 높은 금액과 이름 출력하기

import  blind_auction_art

bid_dics = {} # 이름과 금액을 저장 할 딕셔너리 생성
logo = blind_auction_art.logo
print(logo)

while True : # no 입력까지 진행
    name = input("What's is your name?: ") # 이름
    bid = int(input("What' is your bid: ")) # 금액
    
    bid_dics[name] = bid # 딕셔너리 추가
    
    # 진행 여부 판단
    progress = input("Are there any other bidders? Type 'yas' or 'no': " ).lower()
    
    if progress == "no" :
        max_num = 0
        max_name = ""
        for key in bid_dics:
            bid_num = bid_dics[key]
            if bid_num > max_num : # 최댓값 구하기
                max_name = key
                max_num = bid_num
        
        print(f"The winner is {max_name} with a bid of ${max_num}")    
    
    
    # 메소드 사용하기
    # max(dics_name. key = dics_name.get) # 최댓값(valuse)의 키 값 구하기
    # max(dics_name.values()) # valuse 최댓값 구하기
    # max(dics_name) # 키 값중에 최댓값
    # if progress == "no" :
    #     print(f"The winner is {max(bid_dics, key = bid_dics.get)} with a bid of ${max(bid_dics.values())}")
    #     break
