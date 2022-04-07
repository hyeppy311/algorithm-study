
# N으로 나누었을 때 몫과 나머지가 같은 모든 자연수의 합 

# 검색 

# N=3 일 경우 3*1+1, 3*2+2, 3*3+3.. 

n = int(input())

ans = 0
for i in range(1,n):
  ans += (n*i+i)
print(ans) 


