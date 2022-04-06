# 칸이 2개 이상이면 누울 수 있음
# 가로, 세로 누울자리 개수 구하기 

# 무슨 탐색하는거같은데.. 


# 답은 나오지만 실패..! 

n = int(input())

room = [list(input()) for _ in range(n)]

cnt = 0
col = 0

for i in range(n) :
  for j in range(n) :
    if room[i][j] == '.' :     # 빈자리 일 경우
      cnt += 1                 # 자리를 세어주고 
      if cnt >= 2 :            # 2개 이상이면
        col += 1               # 자리 더해주고 break
        break
    else :                    # 짐이 있는 경우
      cnt = 0                 # 빈자리 리셋
      
      
cnt = 0
row = 0
for i in range(5) :
  for j in range(5) :
    if room[j][i] == '.' :
      cnt += 1
      if cnt >= 2 :
        row += 1
        cnt = 0
        break
    else : 
      cnt = 0

print(col,row)

------------------------------- 

# 검색 


row = 0
column = 0

for y in range(N):
    cnt = 0
    for x in range(N):
        if matrix[y][x] == '.':         # 짐이 없는 경우 칸 1개 추가
            cnt += 1
        elif matrix[y][x] == 'X':       # 짐이 있는 경우
            if cnt >= 2:                # 칸이 2보다 크면
                row += 1                # 누울 자리 1 더해주고
            cnt = 0                     # 자리 초기화 
    if cnt >= 2:                   # 칸이 2이상이면
        row += 1                   # 누울자리에 1 더해주고
    cnt = 0                        # 칸 초기화 
    
# 빈 공간을 세다가 짐이 있는 경우와 아닐 경우를 나눠서 봐야함 
# 내가 작성한 코드에는 빈 공간을 세다가 짐을 만났을 경우만 있음 


