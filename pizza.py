print("Thank you for cgoosing python pizza deliveries!")

siza = input("what size pizza do you want? s, m, or l: ")
add_pepperoni = input("do you want pepperoni? y or n: ")
exter_cheese = input("do you want exter cheese? y or n: ")
 
pizza_price = 0 # 합계 계산

# s= 15& m = 20& l = 25 &
if siza == "s" :
    pizza_price += 15
    if add_pepperoni == "y" : #페퍼로니 추가시 
        pizza_price += 2
        
        
elif siza == "m" : 
    pizza_price += 20
    if add_pepperoni == "y" : #페퍼로니 추가시 
        pizza_price += 3
        
else :
    pizza_price += 25
    if add_pepperoni == "y" : #페퍼로니 추가시 
        pizza_price += 3

if exter_cheese == "y" : # 치즈 추가시
    pizza_price += 1            

# 결과 출력    
print(f"thank you  for choosing python pizza deliveries! \nyour final bill is : &{pizza_price}.")