
n = int(input())
day = list(map(int,(input().split())))

cnt = 0 

for i in day :
  if i == n :
    cnt += 1

print(cnt)



