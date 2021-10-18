n = int(input())

for i in reversed(range(n+1)) :
  s= "*"*i
  print(s.rjust(n))
