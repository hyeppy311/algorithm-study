n = int(input())

for i in range(1,n+1) :
  s= "*"*i
  print(s+" "*((n-i)*2)+s)
for j in range(1,n) :
  s = "*"*(n-j) 
  print(s+" "*(j*2)+s)
