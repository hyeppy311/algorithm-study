## 1차 제출 성공! 

price = [int(input()) for _ in range(10)]

sum_price = price[0]
price.pop(0)
print(sum_price-sum(price))



## 하지만 whlie문으로 풀어보고 싶었던 나..
## 1. while으로 입력값 받기
## 2. 제일 처음 들어오는 값(책 합계)을 따로 변수에 지정
## 3. 나머지 들어오는 값들 변수에 하나씩 더해주고 
## 2에서 3을 뺀다! 

cnt = 1 
price_all = 0

while True :
  price = map(int, input().split())

  if cnt == 11:
    break 
  
  if cnt == 1 :
    price_sum = price
  
  cnt += 1
  price_all += price
  

print(price_sum - price_all)

## 뭔가 계속 시도했지만 잘 안댐.. 

## 검색 고고씽

price_total = int(input())    ##input()은 첫줄을 읽어온다..! 

for i in range(9) :               ## 나머지 값 9개를 for문으로 받으면서 
  price_total -= int(input())     ## price_total에서 뺀다..! 

print(price_total)


## 입력으로 들어오는 맨 처음 값이 합계이고 나머지 값들을 빼주면 답이 나온다..!
## 는건 머릿속으로 알고있었지만 이런방법도 있구나..

