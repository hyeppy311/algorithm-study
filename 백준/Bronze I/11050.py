

import sys
input = sys.stdin.readline

n, k  = map(int, input().split())

import math 
answer = math.factorial(n) // (math.factorial(k)*math.factorial(n-k))

print(answer)

