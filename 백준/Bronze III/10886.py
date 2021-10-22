
n = int(input())

ls = []

for i in range(n) :
  ls.append(int(input()))

if ls.count(0) > ls.count(1) :
  print("Junhee is not cute!")
else :
  print("Junhee is cute!")
