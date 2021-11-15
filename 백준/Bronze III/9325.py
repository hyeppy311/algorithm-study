
## 시도한 코드


t  = int(input())

for _ in range(t) :
  car_price, opts = map(int, input().split())

  if opts >= 1 :
    for _ in range(opts) :
      q,p = map(int, input().split())

      print(car_price + q*p)
  else : 
    print(car_price)
    
    

## 검색한 코드

T = int(input())  # 테스트 케이스

for _ in range(T) :
  s = int(input())        # 자동차의 가격
  n = int(input())        # 옵션의 갯수
  price = s               # 가격 저장 (옵션없을때)
  
  for _ in range(n) :     # 옵션 입력
    q,p = map(int, input().split())
    price += q*p          # 원래 차의 가격에 옵션 더해줌
    
  print(price)
