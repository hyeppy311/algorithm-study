n = int(input())

for i in range(n,0,-1):
  print(' '*(n-i)+'*'*(i*2-1))
for j in range(1,n):
  print(' '*(n-j-1)+"*"*(j*2+1))
