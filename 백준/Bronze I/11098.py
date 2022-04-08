

n = int(input())

for _ in range(n) :
  p = int(input())

  max_p = 0
  tmp = {}
  for _ in range(p) :
    c,name = input().split()
    tmp[int(c)] = name
  for k,v in tmp.items() :
    if k == max(tmp.keys()) :
      print(v)
      
      
    
