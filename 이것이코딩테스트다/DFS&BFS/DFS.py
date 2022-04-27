
# 예제

# 노드가 연결된 정보를 2차원 리스트로 표현

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

# 노드가 방문된 정보를 리스트로 표현 
visited = [False] * 9

# DFS 함수 정의 
def dfs(graph, v, visited) :
  visited[v] = True               # 현재 노드를 방문처리 해주고
  print(v , end=" ")              # 출력
  
  for i in graph[v] :             # 현재 노드와 연결된 다른 노드를 방문
    if not visited[i] :           # 방문하지 않았으면
      dfs(graph , i , visited)    # 다시 함수에 넣기 (재귀적으로 처리함)
      
# 함수 호출      
dfs(graph, 1, visited)

# 출력 
1 2 7 6 8 3 4 5
