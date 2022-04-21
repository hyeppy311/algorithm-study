
# 문제 
# 정수 N , 00시 00분 00초 부터 N시 59분 59초 까지 3이 하나라도 포함하는 모든 경우의 수

# 시도!
# 처음에 이렇게 했는데 왜 안될까..? 

n = int(input())

cnt = 0
for i in range(0,(n*10000)+5960) :    # 시,분,초를 나누지 않고 하는 경우 중복카운트 되서 더 많이 나옴 
  if "3" in str(i) :
    cnt += 1

print(cnt)

# 2번째 시도! 

n = int(input())

cnt = 0
for i in range(0,n*10000+5960) :
  for j in str(i) :
    if j == "3" :
      cnt += 1
 
    

print(cnt)

# 틀림! 



# 답안 예

h = int(input())

count = 0
for i in range(h+1) :           #시각
  for j in range(60) :          #분
    for k in range(60) :        #초 
      if "3" in str(i) + str(j) + str(k) :   # 3이 있으면 1 더해줌 
        count += 1

print(count)


# 시간, 분, 초를 어떻게 나눠야 하나 했는데 for문으로 하나씩..
# for문과 range 
