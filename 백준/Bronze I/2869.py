
# 처음 작성 코드
a, b, v = map(int, input().split())

days = 1
up = 1+a-b

while True :
  up = up + a-b
  days +=1 
  if up >= v :
    break
print(days)

# 나무의 길이 V의 값이 너무 클 경우 시간초과가 뜸 
# a,b,v 의 관계를 파악해서 연산식을 넣어야함 


# 하루에 올라가야하는 거리 (a-b) * days + a가 막대기의 길이보다 길어야한다. 
# 식으로쓰면 (a-b) * days + a > V , days를 계산하려면 v-a / a-b 

import math 

s = math.ceil((v-a)/(a-b))
print(s)
