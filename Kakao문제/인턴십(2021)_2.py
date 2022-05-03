
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
