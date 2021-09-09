a = int(input())

for _ in range(a):
  h,w,n = map(int,input().split())

  if n%h == 0 :
    print((h*100)+(n//h))
  elif n>h : 
    print((n%h)*100+(n//h+1))
  elif n == h :
    print((n*100)+(n//h))
  elif n < h : 
    print((n*100)+1)
    
    
