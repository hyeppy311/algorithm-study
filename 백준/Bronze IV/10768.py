

## 내가 쓴 코드 

month = int(input())
day = int(input())

if month == 1 and 1 <= day <= 31:
  print("Before")

elif month == 2 and 1 <= day <= 17 :
  print('Before')
  
elif month == 2 and day == 18 :
  print("Special")

elif month == 2 and day > 18 :
  print("After")

elif month > 2 and 1<= day <= 31: 
  print("After")
  
 

## 짧은 코드

if month == 2 and day == 18 :
  print('Special')
elif month < 2 or (month == 2 and day <= 17) :    ## 1월은 무조건 Before가 되므로 day조건을 걸어줄 필요가 없음
  print("Before")
else :
  print('After')
  
  
