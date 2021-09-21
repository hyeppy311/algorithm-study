
a,b = map(int,input().split())
c,d = map(int,input().split())

if a+d == c+b :
  print(a+d)
else:
  print(min(a+d,c+b))
