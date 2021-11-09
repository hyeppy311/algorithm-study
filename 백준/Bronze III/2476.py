

n = int(input())

tmp = []
for _ in range(n) :
  a,b,c = map(int, input().split())

  if a==b==c :
    tmp.append(10000+(a*1000))

  elif a==b or b == c or  a==c :
    if a==b :
      tmp.append(1000+(a*100))
    elif b == c :
      tmp.append(1000+(b*100))
    elif a == c :
      tmp.append(1000+(a*100)) 
  else :
    tmp.append(max(a,b,c)*100)

print(max(tmp))
