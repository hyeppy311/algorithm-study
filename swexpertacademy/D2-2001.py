T = int(input())

for t in range(1,T+1) :
  n,m = map(int, input().split())
  arr = [list(map(int,input().split())) for _ in range(n)]
  memo = [[0] * (n+1) for _ in range(n+1)]

  for i in range(1,n+1) :
    for j in range(1,n+1) :
      memo[i][j] = arr[i-1][j-1] + memo[i][j-1] + memo[i-1][j] - memo[i-1][j-1]
  

  for _ in range(n+2) :
    for _ in range(n+2) :
      fly = memo[m+1][m+1] - memo[m-1][m+1] - memo[m+1][m-1] + memo[m-1][m-1]

  print(f'#{t} {fly}')
