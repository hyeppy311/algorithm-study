# 진법변환 (문제가 이해가 안됐음)
# 10진법을 B진법으로 나타낼 때 숫자로 나타낼 수 없는 부분은 알파벳으로 나타냄 

# 진법계산 10진수를 B으로 나누어 떨어지지 않을때 까지 나눔 -> 나머지를 알파벳으로 나타냄 


# 검색

import sys 
s = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"      # 주어진 문제에서 A:10, B:11.. 
N,B = map(int, sys.stdin.readline().split())

ans = ''

while N != 0 :
  ans += s[N % B]   # 나머지가 5이면 s[5] 반환
  N // =B           # 몫을 계속 구해서 while문 돌게함 
  
print(ans[::-1])    # 뒤집어서 출력 
