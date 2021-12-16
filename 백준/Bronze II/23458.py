## 총감독관이 감시할 수 있는 응시자의 수 b, 부감독관이 감시할 수 있는 응시자의 수 c
## 교실의 개수 n , 교실에 있는 응시자의 수 a 

n = int(input())
a = list(map(int,input().split()))
b,c = map(int, input().split())

answer = 0 


for i in a :
  if i <= b :                       ## 응시자의 수가 총감독이 감시할 수 있는 수 보다 작거나 같으면 
    answer += 1 
  elif (i-b)% c == 0 :              ## 응시자의 수에서 총감독 감시 응시생을 빼고 부감독 감시 응시생으로 나눈 나머지가 0이면
    answer += 1 + (i-b)//c          ## 총감독관 1명이 들어가고 몫(부감독관 감시 응시생)을 더해줌
  elif (i-b) % c != 0 :             ## 0이 아니라면
    answer += 1 + (i-b)//c + 1      ## 총감독관 1명, 부감독관의 수, 1(나머지 응시생 부감독관이 감시)를 더해줌

print(answer)
