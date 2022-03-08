# 시간초과되서 sys 했는데 계속 시간초과 뜸.. 

import sys 

input = sys.stdin.readline

num_1,num_2 = map(str, input().split())

ans = 0
for i in range(len(num_1)) :
  for j in range(len(num_2)) :
    ans += int(num_1[i])*int(num_2[j])

print(ans)
  

## ab, cd 두 숫자가 있을때 
# a*c + b*d -> (a+b)*(c+d)라는 것을 알아야 함.. 


n1, n2 = input().split()
n1, n2 = list(map(int, n1)) , list(map(int, n2))

print(sum(n1)*sum(n2))
