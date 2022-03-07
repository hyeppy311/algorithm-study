# 맨 마지막 막대기의 길이를 왼쪽으로 가면서 하나씩 비교
# 맨 마지막 막대기가 제일 길면 하나만 보임 
# 맨 마지막 막대기가 제일 짧으면 비교하여 큰 값들 빈 리스트에 저장

import sys

input = sys.stdin.readline

n = int(input())

h = [int(input()) for _ in range(n)]

stick = 0
for i in range(n-2,-1,-1) :
  if h[-1] < h[i] :        ## 끝에  1234
    stick += 1
  elif h[-1] == h[i] :
    stick + 1
  else :
    stick = 1
  

print(stick)

# 실패..! 


## 검색
ans = 1      # 맨 오른쪽 막대기는 무조건 포함(항상 보이기 떄문)
Max = h[-1]  # 최대값은 막대기의 맨 오른쪽 

for i in rnage(n-1,-1,-1) :    ## 오른쪽에서 왼쪽으로 가면서
  if h[i] > Max :              # 맨 오른쪽의 막대기보다 왼쪽막대기가 크면
      ans += 1                 # 갯수 추가
      Max = h[i]               # 다시 큰 값으로 바꿔줌

print(ans)



## 다른코드 

import sys
input = sys.stdin.readline
 
n = int(input())
sticks = [int(input()) for _ in range(n)]
max_height = sticks[-1]
cnt = 1
 
for i in range(n):
    temp = sticks.pop()      ## pop를 사용(맨 오른쪽에서부터 왼쪽으로 원소를 뽑음) # range를 역순으로 할 필요가 없음
    if max_height < temp:
        cnt += 1
        max_height = temp
print(cnt)

