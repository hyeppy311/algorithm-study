

n = int(input())

for i in range(1,n+1) :
  s= "*"*(i*2-1)
  print(" "*(n-i)+s)
for j in range(n,1,-1) :
  s = "*"*(j*2-3) 
  print(" "*(n-j+1)+s)

