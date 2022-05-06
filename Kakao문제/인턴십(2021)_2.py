
# 어떻게 풀어야될지 감도안옴.. 
# P를 중심으로 2만큼 거리에 또 다른 P가 있는지 확인? 
# 만약에 하나라도 있으면 그냥 1 넣어줌? 


# 먼저 P의 위치를 저장 
# P의 위치에 상,하,좌,우 2만큼 움직이는 리스트 선언 
# 그 안에 P가 있으면 1 answer에 넣어줌 

moves = [(0,1),(0,2),(1,0),(2,0),(0,-1),(0,-2),(-1,0),(-2,0)]

ans = []
for place in places :
  for i in range(5) :
    for j in range(5) :
      if place[i][j] == "P":
        x,y= i,j
        for move in moves :
          next_x = x+move[0]
          next_y = y+move[1]
       
          if 0<=next_x<=4 and 0<=next_y<=4 and place[next_x][place][next_y] == "P" :   ## 범위 벗어나는 경우 다시 설정 
            ans.append(1)
            
          else :
            ans.append(0)
print(ans)


# 문제접근방법 
# - 각 자리를 하나의 정점으로 본다.
# - 2만큼씩 이동해서 P가 있는지 확인한다.
# - P를 만나지 않으면 1, P를 만나면 0를 추가한다. 
# - BFS를 이용한다. 

## 검색

# 1. 기본 함수 구현 

def solution(places):
    answer = []
    for place in places:
        if check(place):
            answer.append(1)
        else:
            answer.append(0)
    return answer
  
# 2. 거리두기 확인 함수 구현
def check(place):
    for i in range(len(place)):
        for j in range(len(place)):
            if place[i][j] == 'P':             # P가 있으면
                if not bfs(i, j, place):       # bfs 함수에 넣고 P를 만나면 
                    return False               # False 반환 
    return True   # 2중 포문을 돌면서 False를 반환하지 않을 경우 True 반환 
  

# 3. P의 위치를 확인 할 bfs 함수 구현 

from collections import deque

dx = [-1, 1, 0, 0]        # 상하좌우 움직일 수 있는 좌표 선언
dy = [0, 0, -1, 1]

def bfs(x, y, place):          # bfs 함수 정의, x,y = i,j (place의 인덱스)
    visited = [[0] *5 for _ in range(5)]  # 방문처리 할 빈 리스트 생성 
    queue = deque()                       # 큐 객체 생성
    queue.append((x,y,0))                 # deque([(x, y, 0)]) 
    visited[x][y] = 1                     # 방문한 곳 체크 

    while queue:
        x, y, dist = queue.popleft()     # 먼저 들어간 값을 뽑아 변수에 저장 
       
        if 0 < dist < 3 and place[x][y] == 'P':    # 거리두기를 하지 않았을 경우 False 반환 -> check()에서 False 반환 -> answer에 0 추가 
            return False
        if dist > 2:                              # 거리가 2보다 크면 볼 필요 없으므로 멈춤
            break
        for i in range(4):                        # 현재 위치에서 상하 좌우 움직이고
            nx = x + dx[i]
            ny = y + dy[i]                        
            nd = dist + 1                         # 거리도 1씩 늘려줌 
             # 배열의 크기 안에 있고, 파티션이 아니고, 방문한 적이 없다면
            if 0 <= nx < 5 and 0 <= ny < 5 and place[nx][ny] != 'X' and not visited[nx][ny]:   
                queue.append((nx,ny, nd))       # dueue에 좌표와 거리 추가
                visited[nx][ny] = 1             # 방문처리 
    return True                                 # 방문이 끝나면 True반환 
 
# 전체 코드 
  
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, place):
    visited = [[0] *5 for _ in range(5)]
    queue = deque()
    queue.append((x,y,0))
    visited[x][y] = 1

    while queue:
        x, y, dist = queue.popleft()
       
        if 0 < dist < 3 and place[x][y] == 'P':
            return False
        if dist > 2:
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            nd = dist + 1
           
            if 0 <= nx < 5 and 0 <= ny < 5 and place[nx][ny] != 'X' and not visited[nx][ny]:
                queue.append((nx,ny, nd))
                visited[nx][ny] = 1
    return True

def check(place):
    for i in range(len(place)):
        for j in range(len(place)):
            if place[i][j] == 'P':
                if not bfs(i, j, place):
                    return False
    return True 

def solution(places):
    answer = []
    for place in places:
        if check(place):
            answer.append(1)
        else:
            answer.append(0)
    return answer  
