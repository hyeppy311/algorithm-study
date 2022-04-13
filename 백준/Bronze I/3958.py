
# 입력받은 값에 번호를 어떻게 줄 것인가..? 
# 딕셔너리? 

L = int(input())
N = int(input())

tmp = dict()
for i in range(1,N+1) :
  p,k = map(int, input().split())
  tmp[i] = p,k       # 방청객 번호와 케이크 조각 길이 p~k까지 담은 딕셔너리
  

cake = [0] * L        # 케이크 길이만큼 0 리스트 생성
for j in tmp.keys() :
  for p,k in tmp.values() :
    cake[p-1:k-1] = [j]*N      # 방청객이 원하는 길이에 방청객 번호를 넣으려고 했는데 리스트는 브로드캐스팅을 지원안함. list[a:b] = 1 안됨
    

    

# 검색

L = int(input())
N = int(input()) 

cake = [0] * (L+1)
take = [0] * (N+1)
maxCake, maxNum = 0,0

# 방청객이 원하는 케이크 조각 입력 

for i in range (1,N+1) :
  cnt = 0
  p,k = map(int, input().split())
  pieces = k-p+1              # 가장 많이 받을 것으로 기대한 방청객
  if maxCake < pieces :       # 원하는 조각 수를 입력받아 크기 비교 후 
    maxCake = pieces          # 최대값으로 저장
    maxNum = i                 # 방청객 번호
    
  for j in range(p,k + 1 ) :   # 실제로 받는 케이크 조각
    if cake[j] == 0 :          # 원하는 부분이 0이면
      cake[j] = i              # 원하는 부분에 방청객 번호 입력
      cnt += 1                 # 카운트 +1 
  take[i] = cnt

print(maxNum)             # 기대한 방청객 번호
print(take.index(max(cake)))    # 실제로 많이 받은 방청객


