
## 못풀었다!! 

x_ls = []
y_ls = []

for i in range(3) :
  x,y = map(int,input().split())
  x_ls.append(x)
  y_ls.append(y)

for j in range(3): 
  if x_ls.count(x_ls[j]) == 1:
    x_ = x_ls[j]
  if y_ls.count(y_ls[j]) == 1: 
    y_ = y_ls[j]

print(x_,y_)


## x,y 4개의 좌표에서 x값이 같은 것이 2개씩 2개, y도 마찬가지로 같은 값이 2개씩 2개가 있다.
## x,y의 값을 각각 리스트에 담고 x,y의 값이 하나인 것을 변수에 담아 출력 


