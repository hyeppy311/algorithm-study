
minkuk = list(map(int, input().split()))
manse = list(map(int, input().split()))

s = sum(minkuk)
t = sum(manse)

if s == t :
  print(s)
else : 
  print(max(s,t))
  
  
  
