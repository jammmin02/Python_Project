def greet():
    print("hello")
    print("안녕")
    print("좋은 하루")
    
def  greet_name(name):
    print(f"hello {name}")
    print(f"안녕{name}")
    print(f"좋은 하루{name}")

# greet_name("jungmin")

# name = parameter (파라미터) -> 아규먼트(데이터)의 이름으로 함수 안에서 그 변수가 사용될때 쓰임
# jungmin = argement (아규먼트) ->함수로 전달되고 호출되는 데이터 (데이터의 실제 값)

def greet_with(name, location):
    print(f"hello {name}")
    print(f"my location is {location}")
    
greet_with("jumg", "대구") # 위치 인자
greet_with(location="대구", name="jung") # 키워드 인자
    