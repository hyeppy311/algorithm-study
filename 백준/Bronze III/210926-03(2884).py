

h,m = map(int, input().split())

a = m-45 

if a < 0 :
  if h == 0 :
    print(23, m+15)
  else : 
    print(h-1 , m + 15)
elif a >= 0 :
 print(h, a)


