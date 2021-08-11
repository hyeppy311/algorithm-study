# 내가 푼 답

n,x = map(int,input().split())
a = list(range(1,1+n))

for i in a : 
  if i < x :
    print(i, end = ' ')
    
