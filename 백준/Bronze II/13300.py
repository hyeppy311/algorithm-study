# 학년으로 나눈 후 성별로 나눈다
# 성별로 나눈 후 학년으로 나눈다




n, k = map(int, input().split())

lst = [[0]*6 for _ in range(2)]        # 빈 리스트를 만들어 주는게 ..!! 

for _ in range(n) :
  s,y = map(int, input().split())

  if s == 0 :
    lst[0][y-1] +=1
  else :
    lst[1][y-1] +=1

  # 간단하게 
  # lst[s][y-1] +=1
    

room = 0 

for i in lst :
  for j in i :
    if j % k == 0:        # 인원수와 방 갯수가 나눠 떨어지면 
      room += j/k         # 학생수가 0명일 경우도 있어서 
    else: 
      room += j//k + 1    # 인원수 초과 할 경우 방 갯수랑 나머지 방 1개 더해줌 
    # if 1 <= j < k :
    #   room += 1
    # elif j % k == 0 :
    #   room += j//k
    # elif j % k != 0 :
    #   room += j//k + 1
    # else :
    #   pass
  
print(int(room))
