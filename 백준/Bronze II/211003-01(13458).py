
n = int(input())
a = list(map(int, input().split()))
b,c = map(int, input().split())

supervi = []
for i in a :
  supervi.append(i-b)
  # print(supervi)
  
vice = []
for j in supervi :
  if j<b :
    vice.append(j//b+1)
  elif j>b :
    vice.append(j//b+1)
      # print(vice)
  else :
    vice.append(j//b)
      # print(vice)
print(sum(vice)+n)
   
