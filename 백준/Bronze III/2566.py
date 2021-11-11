
'''
1. 2차원 리스트로 입력
2. for문으로 각 리스트의 최대값 빈 리스트에 담기
3. 2번의 리스트에서 최대값의 인덱스가 행이 됨 
4. 
'''


lst = [list(map(int,input().split())) for _ in range(9)]  ## 2차원 리스트 입력 

tmp = []
for i in lst :
  tmp.append(max(i))                        ## 리스트 안 리스트의 최대값을 담아줌
  
  for idx, val in enumerate(i) :            ## 최대값의 위치(열)를 리스트 내에서 찾아줌
    if max(tmp) == val :
      a = idx

print(max(tmp))                             ## 최대값 출력
print(tmp.index(max(tmp))+1, a+1)           ## 행,열 출력


## 최대값이 2개 이상이면 한 곳의 위치를 출력


lst = [list(map(int,input().split())) for _ in range(9)]

tmp = []
for i in lst :
  tmp.append(max(i))
  
  
  for idx, val in enumerate(i) :

    if max(tmp) >= 2 :    ## 최대값의 갯수를 어떻게 센담..? 
      a = max(tmp)
    elif max(tmp) == val :
      b = idx 

print(max(tmp))
print(tmp.index(max(tmp))+1, b+1)
print(tmp.index(a)+1, b+1)

