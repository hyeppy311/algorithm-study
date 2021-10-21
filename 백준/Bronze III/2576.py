## 제출실패

numbers = [int(input()) for _ in range(7)]

temp = []
for i in numbers :
  if i % 2 != 0:          ## 홀수일때 빈 리스트에 넣어주고
    temp.append(i)        ## 만약에 리스트 비어있으면 (-1)
    if temp == [] :
      print(-1)
 
print(sum(temp))          ## 합과 최소값 출력..
print(min(temp))



## 검색 후 수정


numbers = [int(input()) for _ in range(7)]

temp = []
for i in numbers :
  if i % 2 != 0:
    temp.append(i)

if temp :               ## 참이되는 조건(리스트에 값이 있음)이 되면 홀수만 있으니까 합,최소값 출력
  print(sum(temp))
  print(min(temp))
else :                  ## 리스트가 비어있으면 (모두 짝수) -1 출력
  print(-1)
