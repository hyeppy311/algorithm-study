

# Counter 함수 써봤는데 틀림 ㅠㅠ

from collections import Counter

n = int(input())
# Counter로 시도 -> 실패... 

for _ in range(n) :
  a,b = input().split()

  word_a = Counter(a)
  word_b = Counter(b)

  if word_a == word_b :
    print(f'{a} & {b} are anagrams.')
  else: 
    print(f'{a} & {b} are not anagrams.')
    
 

# 검색

import sys

input = sys.stdin.readline

t = int(input())

for i in range(t):
    a, b = map(str, input().split())
    
    x = sorted(list(a))           # 
    y = sorted(list(b))

    if x == y:
        print("%s & %s are anagrams." %(a, b))
    else:
        print("%s & %s are NOT anagrams." %(a, b))
        
 
# sort를 생각했었는데 리스트로 입력시 리스트로 변환하는 것 부터 막혔음.. 
# sort와 sorted를 다시 공부해야될듯 

