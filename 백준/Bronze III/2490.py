
## while문 실패 후 입력 수정 

n = [list(map(int,input().split())) for _ in range(3)]   ## 2차원 리스트로 받아서 

for i in range(3) :             ## 원소(리스트) 합을 구해서 출력 
  if sum(n[i]) == 1 :
    print("C")
  elif sum(n[i]) == 2 :
    print("B")
  elif sum(n[i]) == 3 :
    print("A")
  elif sum(n[i]) == 4 :
    print("E")
  else :
    print("D")
    
    
    
## while문 수정  -> 탈출 걸어줌

while True :
  try :

    play = list(map(int,input().split()))
    if sum(play) == 1 :
      print("C")
      
    elif sum(play) == 2 :
      print("B")
      
    elif sum(play) == 3 :
      print("A")
      
    elif sum(play) == 4 :
      print("E")

    else :
      print("D")
  except :
    break
    
    
## try, except 없이 break

cnt = 0

while True :
  play = list(map(int,input().split()))

  if sum(play) == 1 :
    print("C")
    
  elif sum(play) == 2 :
    print("B")
    
  elif sum(play) == 3 :
    print("A")
    
  elif sum(play) == 4 :
    print("E")

  else :
    print("D")

  if cnt == 2:
    break
  
  cnt += 1
  
## while문은 무한루프이다 -> 탈출이 필요함.
## 몇 번 돌릴것인지 횟수를 꼭 지정해줘야함 
## 조건이 맞으면 탈출하는 코드도 넣어주기 


