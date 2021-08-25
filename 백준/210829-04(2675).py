n = int(input())

for _ in range(n) : 
  a,b = input().split()
  a = int(a)

  for i in b : 
    print(i*a, end = '')   ## 가로쓰기
  print()                  ## Enter같은 역할을 함, 한 줄 띄우기 
