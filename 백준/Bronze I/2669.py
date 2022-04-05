# 평면에 놓인 4개의 직사각형의 넓이 구하기
# 겹칠 수도 있고 겹치지 않을 수도 있다. 

# 색종이 문제에서 처럼 0으로 채워진 2차원 리스트를 만들어서 
# 사각형의 내부를 1로 쪼개서 2차원 리스트에 저장 


# 시도 ==> 답은 나왔는데 틀렸음 

for _ in range(4) :
  L_x,L_y,R_x,R_y = map(int, input().split())
  
  tmp = [[0] * 100 for _ in range(100)]  # range 범위 잘못됨 

  for i in range(R_x-L_x-1, R_x+1):    # 오른쪽 위 꼭지점으로 사각형을 카운트했는데 굳이 이렇게 할 필요 없었음  
    for j in range(R_y-L_y, R_y+1) :
      tmp[j][i] = 1

cnt = 0
for i in tmp :
  cnt += sum(i)
print(cnt)


# 검색

paper = [[0 for _ in range(101)] for _ in range(101)]    

for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    
    #사각형 부분만 1로 바꾸어줌
    for i in range(x1, x2):          # 입력받은 좌표를 그냥 넣어주면 됨 
        for j in range(y1, y2):
            paper[i][j] = 1

answer = 0
for row in paper:
    answer += sum(row)
print(answer)


