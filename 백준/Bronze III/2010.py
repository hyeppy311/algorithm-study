

import sys
input = sys.stdin.readline

n = int(input())

total = 0

for _ in range(n) :
  tap = int(input()) 
  total += tap     ## 플러그의 갯수를 다 더해주고    

print(total-(n-1))    ## 플러그의 갯수에서 멀티탭 갯수 - 1 (마지막 멀티탭은 연결되는게 없음)
