# 새 딕셔너리를 travel_log에 넣는 함수 작성
def new_countries(counrty_name, visits_num, citi_name):
    new_country = {}
    new_country["counrty"] = counrty_name
    new_country["visits"] = visits_num
    new_country["cities"] = citi_name
    travel_log.append(new_country)
    print(travel_log)

country = input("country name? ") # 나라 이름
visits = int(input("visits num? ")) # 방문 횟수
list_of_cities = eval(input("cities name? ")) # 방문한 도시 

# 기본 리스트
travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]

new_countries(country, visits,list_of_cities)