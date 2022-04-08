
# numpy로 계산했지만 모듈 지원 안함..ㅠㅠ

import numpy as np
n,m = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(n)]

A = np.array(a)
B = np.array(b)
sums = A+B 

for i in range(len(A)):
  for j in range(len(B)):
    print(sums[i][j], end=' ')
  print()



# 직접계산 -> indexerror 

n,m = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(n)]

ans = [[0]*m for _ in range(n)]

for i in range(n) :
  for j in range(m) :
    ans[i][j] = a[i][j] + b[i][j]

for i in range(len(a)) :
  for j in range(len(b)) :
    print(ans[i][j], end=" ")
  print()
  

 # 검색해서 수정

n,m = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(n)]

for i in range(n) :
  for j in range(m) :
    a[i][j] += b[i][j]       # 행렬 덧셈은 같은 위치끼리 더하기 때문에 A리스트에 B리스트의 원소를 더해주기만 하면됨
  print(*a[i])          # m 만큼 line 49 반복 한 후 a[i]위치 값 출력

