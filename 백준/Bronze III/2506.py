

n = int(input())

score = list(map(int,input().split()))

cnt, result = 0,0

for i in range(n) :
  if score[i] == 1 : 
    cnt += 1          ## 하나씩 올려준 값
    result += cnt     ## 전부 더해주는 부분
  
  else :
    cnt =  0

print(result)
