# 윤년인지 확인하는 함수
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
    
# 일 수를 출력하는 함수
def days_in_month(month_year, month_days):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
  is_leap(month_year)
  if month == 2 and is_leap(year):
      return 29
  else :
      return month_days[month-1]
      

year = int(input("Enter a year: ")) 
month = int(input("Enter a month: "))

print(days_in_month(year, month))
