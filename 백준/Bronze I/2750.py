
n = int(input())

ans = []
for _ in range(n) :
  ans.append(int(input()))
  ans.sort(reverse = False)

print(*ans, sep = '\n')



# 이전코드 

n = int(input())

nums = sorted([int(input()) for _ in range(n)])
               
print(*nums, sep = '\n')
