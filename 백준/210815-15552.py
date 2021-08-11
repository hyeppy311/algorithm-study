import sys  # 매개변수 직접 주기 가능

a = sys.stdin.readline().strip()
c,d = map(int,sys.stdin.readline().split()) # 입력을 a로 받은 값 만큼 어떻게 나타낸담..? -> range

nums = [a]
for i in nums :
  print(c+d)  

# readline() 입력된 첫번째줄 읽어줌
# readlines() 모든 줄을 읽어서 리스트로 돌려줌

# input = sys.stdin.readline
# strip() 인자없을 경우 왼쪽 공백제거, 있을경우 인자제거


# 답 

import sys  # 모듈 불러오기

t = int(sys.stdin.readline())  # 입력값 변수지정 t = int(input())과 같음

for _ in range(t):             # _(언더바)는 일반 변수처럼 사용 가능 # range : 입력받은 수 만큼 0부터 출력
    a,b = map(int, sys.stdin.readline().split())    # map(int,input().split()) 
    print(a+b)

    
input = sys.stdin.readline   # input으로 치환하면 코드가 좀 더 보기좋을까나~

t = int(input())
for _ in range(t):
  a,b = map(int, input().split())
  print(a+b) 


# sys는 자세하게 알 필요는 없고...공부할때는 input정도만 알고있어도 됨 
