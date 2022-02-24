

n = int(input())

order =[i for i in range(1,n+1)]
lst = list(map(int, input().split()))

print(order)

tmp = order[0]
order[lst[1]-1] = order[1]
order[1] =tmp

print(order)

tmp= order[1]
order[lst[2]]= order[2]
order[2] = tmp

print(order)

tmp = order[lst[3]-3]
order[lst[3]-3] = order[3]
order[3] = tmp

print(order)

## 여기까지 시도했을 때 자리바꾸기가 아니라 순서가 바뀔때 뒤에 있는 사람이 밀려난다는걸 알았다.. 

## 검색한 코드 

import sys 
input = sys.stdin.readline

n = int(input())

lst = list(map(int, input().split()))

ans = []

for i in range(1,n+1) :
  ans.insert(lst[i-1],i)

print(*ans[::-1])


## insert함수를 이용하여 바로 넣어줄 수 있다.. 
