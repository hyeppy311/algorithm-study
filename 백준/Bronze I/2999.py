
# 문자열의 개수를 파악 
# 개수를 R*C (R<=C)로 나타내고
# 문자열을 R*C 행렬에 집어넣고 
# 1행..2행..순으로 정렬 한 뒤 출력 


# 입력과 문자열 개수, r*c 행렬 
encode = input()


nums = [i for i in range(1,len(encode)+1)]

r = 0
c = 0
for i in nums :
  if len(encode) % i ==  0 and len(encode) // i >= i :
    c = len(encode) // i
    r = i


# 2차원 리스트에 추가하는게 잘 안됨

tmp = [[]*r for _ in range(c)]


for i in range(c+1) :
  for j in range(r+1) :
    tmp[j][i] == encode[]


# 검색
tmp = [[] for _ in range(r)]
cnt = 0 

for i in range(c):
  for j in range(r):
    tmp[j].append(encode[cnt])
    cnt += 1 

for i in range(r) :
  print(" ".join(tmp[i]), end=" ")


# 제출 코드 

encode = input()

r = 0  # 행
c = 0  # 열

for i in range(1,len(encode)+1) :                           # 행렬 구하는 부분
   if len(encode) % i ==  0 and len(encode) // i >= i :
    c = len(encode) // i
    r = i

tmp = [[] for _ in range(r)]
cnt = 0 

for i in range(c):
  for j in range(r): 
    tmp[j].append(encode[cnt])    # 계속 이부분에서 막혔는데 index를 어떻게 증가시켜야 할지 몰랐음. 
                                  # tmp[][] 이렇게 안해도 들어감..어차피 i는 계속 돌기때문에 따로 지정 안해줘도 됨
    cnt += 1                      # index값 늘려주기

for i in tmp :
  print("".join(i), end="")
