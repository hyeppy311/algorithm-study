

n = int(input())

nums = [int(input()) for _ in range(n)]

for i in nums :
  if i % 2 == 0 :
    print('even')
  else :
    print('odd')
