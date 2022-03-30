# 입력부터 난관 
# 2차원 배열 형태 [[],[]]

# 시도 
n,m = map(int, input().split())

arr = [list(map(int,input().split())) for _ in range(n)]

k = int(input())

for _ in range(k) :
  i,j,x,y = map(int, input().split())
  arr_sum = 0
  for p in range(i,j) :
    for q in range(x,y) :
      arr_sum += arr[i][j] + arr[x][y] 
  
  print(arr_sum)
 
#실패! 

# 2차 ->  실패 
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
  
  
  
