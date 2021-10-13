n,m = map(int,input().split())
a = (n+m)//2
b = n-a 

if n+m < 0 or n-m < 0 or (n+m)%2 > 0  :
  print(-1)

else :
  print(max(a,b),min(a,b))
