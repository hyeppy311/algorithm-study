
## 리스트 비교하기 

c = list(map(int,input().split()))
asc = [1,2,3,4,5,6,7,8]
des = [8,7,6,5,4,3,2,1]

if c == asc :
  print('ascending')
elif c == des :
  print('descending')
else :
  print('mixed')
