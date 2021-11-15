## 시도한 코드

n = int(input()) 
call_time = list(map(int, input().split()))

price_y = 0
for i in call_time : 
  if 0 < i <= 29 :
    price_y += 10
  else :
    price_y += 20

price_m = 0
for j in call_time :
  if 0 < i <= 59 :
    price_m += 15
  else : 
    price_m += 30

if price_y > price_m :
  print(f'M {price_m}')
elif price_y == price_m :
  print(f'Y M {price_y}')
else :
  print(f'Y {price_y}')

## 문제에서 요구하는 부분을 잘 파악하도록!
  
  

## 검색한 코드

n = int(input()) 
s = list(map(int,input().split())) 

y = 0 
m = 0 
for i in s: 
    y += i // 30 * 10 + 10   ## 30초 마다 10원씩 청구 
    m += i // 60 * 15 + 15   ## 60초 마다 15원씩 청구 
if y < m: 
    print('Y',y) 
elif y > m: 
    print('M %d' % m) 
else: 
    print('Y M %d' % y)
