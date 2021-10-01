## 첫번째 시도 틀!

a,b = map(int, input().split())

print(b-a-1)

for i in range(a+1,b) :
  print(i, end=' ')
  
  
## 두번째 시도 틀! 맞왜틀..? 

a,b = map(int, input().split())


ls = []
for i in range(a+1,b) :
  ls.append(i)
print(len(ls))
print(*ls)


## 만약에 a>b 이거나, b<a 일 수도 있고 두 수 사이에 숫자가 없는 경우(9, 10)가 존재하는 경우를 따져줘야댐... 

if a!=b :
  if a > b :
    a,b = b,a 
  print(b-a-1)
  print(*range(a+1,b))
else:
  print(0)
