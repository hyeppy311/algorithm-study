
# N*N 공간에 여행자의 이동경로 파악하여 최종 도착지점의 좌표를 공백으로 구분하여 출력
# 입력 : 첫째줄에 N, 둘째줄에 이동경로 (L,R,U,D) 

# 입력예시 
# 5
# R R R U D D 


n = int(input())
x,y = 1,1                    # 시작점 설정 
plans = input().split()

dx = [0,0,-1,1]             # U일 경우 x좌표에서 -1, D일 경우 x좌표에서 +1
dy = [-1,1,0,0]             # L일 경우 y좌표에서 -1, R일 경우 y좌표에서 +1 
move_types = ["L", "R", "U", "D"]  # 움직이는 유형 저장 

for plan in plans :                       # if문과 2중 for문 쓰는 경우 잘 봐두기 
  for i in range(len(move_types)) :       # 움직이는 유형만큼 for문 반복하면서
    if plan == move_types[i]:             # 입력으로 받은 이동유형 값이 리스트에 있으면
      nx = x + dx[i]                      # 처음 시작점에서 이동만큼 값을 계산 
      ny = y + dy[i]
      
  if nx < 1 or ny < 1 or nx > n or ny > n :     # 음수가 되는 경우, n의 크기를 벗어나는 경우 무시(공간이탈) 
    continue  
  x,y = nx, ny                                  # 그대로 좌표를 저장하고 다시 반복 
  
print(x,y)                                      # 좌표 출력 




