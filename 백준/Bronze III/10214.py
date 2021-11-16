
# 시도한 코드

t = int(input())

for _ in range(9) :
  y,k = map(int,input().split())

  if y > k :
    print("Yonsei")
  elif y < k :
    print("Korea")
  else :
    print("Draw")
    
    

 ## 검색한 코드


t = int(input())        ## 테스트 케이스의 수
for _ in range(t) :     ## t개의 테스트케이스 (야구 경기 하나)
  Y=K=0
  
  for _ in range(9) :    ## 테스트케이스 (만약 t가 3이라면 27줄)
    y,k = map(int,input().split())
    Y += y        
    K += k
    
  if Y > K :
    print("Yonsei")
  elif Y < K :
    print("Korea")
  else :
    print("Draw")
    
    
    
