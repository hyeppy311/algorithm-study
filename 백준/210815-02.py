
# 내가 시도한 코드 
n = int(input())
num = [1,2,3,4,5,6,7,8,9]

for i in num:
  print(n*i) # 이부분에서 포맷팅을 하면 될 것 같았는데.. 

  
# 포맷팅 찾다가 발견한 코드 

n = int(input())

for y in range(1, 10):
  print(f'{n} * {y} = {n*y}')
  


# range 출력확인  
for y in range(1, 10):
  print(y)
>>>
1
2
3
4
5
6
7
8
9
