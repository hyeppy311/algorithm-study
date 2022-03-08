

n = int(input())

for _ in range(n) :
  num,string= input().split()
  
  temp = []
  for i in string :
    temp.append(i)
  temp.pop(int(num)-1)
  print(''.join(temp))


## indent 잘 맞춰서 쓰고..
## 차근차근 출력 하나씩 해보기..! 
