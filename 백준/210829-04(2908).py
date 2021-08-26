
a,b = input().split()

a = int(a[::-1])      ## slice : [start:stop:step]
b = int(b[::-1])

if a > b :
  print(a)
else :
  print(b)
