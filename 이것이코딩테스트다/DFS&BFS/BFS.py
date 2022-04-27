

graph = [
  [],
  [2,3,8],
  [1,7],
  [1,4,5],
  [3,5],
  [3,4],
  [7],
  [2,6,8],
  [1,7]
] 

visited = [False] * 9

from collections import deque    # queue 리스트 구현을 위해 deque 라이브러리 사용 


def bfs(graph, start, visited) :
  queue = deque([start])             # deque 리스트에 1부터 차례대로 넣어줌  deque[1]
  
  visited[start] = True             # 현재 노드를 방문 처리 
  
  while queue :                    # queue가 빌 때까지 계속 반복
    v = queue.popleft()            # 가장 먼저 들어간 원소를 변수에 저장
    print(v, end= " ")             # 출력 
      
    for i in graph[v] :
      if not visited[i] :        # 방문처리 되지 않았으면
        queue.append(i)          # queue 리스트에 추가
        visited[i] = True        # 방문처리 

bfs(graph,1,visited)
