
n = int(input())

for i in range(1,n+1) :               # range 1부터 출력 
  a,b = map(int, input().split())
  print(f'Case #{i}: {a+b}')
