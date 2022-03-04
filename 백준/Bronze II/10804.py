# 인덱스로 역배치할 부분만 뽑아서 reverse 적용했더니 안됨 
# insert도 시도해봤지만 안됨.. 


import sys

input = sys.stdin.readline

card = [i for i in range(1,21)]

for _ in range(10) :    
  a,b = map(int,input().split())
  a-=1   
  card[a:b] = card[a:b][::-1]

print(*card)





