# 입력부터 난관 
# 2차원 배열 형태 [[],[]]

# 시도 
n,m = map(int, input().split())

arr = [list(map(int,input().split())) for _ in range(n)]    # 2차원 리스트 입력 

k = int(input())

for _ in range(k) :
  i,j,x,y = map(int, input().split())
  arr_sum = 0
  for p in range(i,j) :
    for q in range(x,y) :
      arr_sum += arr[i][j] + arr[x][y] 
  
  print(arr_sum)
 
#실패! 

# 2차 ->  실패 (시간초과) 
n,m = map(int, input().split())

arr = [list(map(int,input().split())) for _ in range(n)]

k = int(input())

for _ in range(k) :
  i,j,x,y = map(int, input().split())
  arr_sum = 0
  for p in range(i-1,x) :      # 리스트 범위 설정 수정 
    for q in range(j-1,y) :
      arr_sum += arr[p][q]     # 변수 수정 
      
  print(arr_sum)
  
  
  
# 검색

import sys
input = sys.stdin.readline
 
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
memo = [[0] * (m+1) for _ in range(n+1)]   # [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]] arr의 합을 넣어줄 리스트 생성 
                                           # 0을 넣어주는 이유는 인덱스 관리를 좀 더 편하게 하기위함 
 
for i in range(1, n+1):
    for j in range(1, m+1):
        memo[i][j] = arr[i-1][j-1] + memo[i][j-1] + memo[i-1][j] - memo[i-1][j-1]  # memo 리스트에 arr의 합을 계산해서 넣어줌
                                                                                   # [[0, 0, 0, 0], [0, 1, 3, 7], [0, 9, 27, 63]]
                                                                                   # memo의 누적합 = arr의 값에 memo[i][j]의 왼쪽 값 memo[i][j-1]과
                                                                                   # 윗쪽값 memo[i-1][j]을 더한 후 대각선의 값을 빼줌 memo[i-1][j-1]
k = int(input())
for _ in range(k):
    i, j, x, y = map(int, input().split())
    print(memo[x][y] - memo[i-1][y] - memo[x][j-1] + memo[i-1][j-1])    # i,j~ x,y의 구간 합은 x,y를 제외한 범위를 빼주고 중복으로 빠진 부분은 더해준다.
    


# 누적 합을 구할 때는 더해 준 후 중복값을 빼주고 
# 구간 합을 구할 때는 빼준 후 중복값을 더해준다. 

# 동적프로그래밍 
# memoization : 이미 저장된 값을 계속 꺼내서 쓰는 방법 -> 시간복잡도를 줄일 수 있다. 

