def my_function():
    result = 3 * 2
    return result

# 함수의 output

def formet_name(f_name, l_name):
    """연습함수야 
    연습!"""
    if f_name == "" or l_name == "":
        return "질문 똑바로 안읽냐"
    print(f_name.title())
    print(l_name.title())
    

print(formet_name(input("what is your name"),
      input("What es tour last name? ")))


    