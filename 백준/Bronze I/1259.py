
# int를 str으로 list로 입력
# 리스트의 왼쪽과 오른쪽을 가운데로 옮겨가며 비교 -> reverse 함수 사용


import sys

input = sys.stdin.readline

while True :
  n = list(map(str, input().rstrip()))
  if "0" in n :           # 리스트 안에 0이 포함되는 수도 있기때문에 수정 
    break
    
  if len(n) % 2 != 0 :
    ls = list(reversed(n))
    print(ls)
    if n == ls :
      print('yes')
  else : 
    print('no')

# reversed 함수를 이용했지만 실패...!



import sys

input = sys.stdin.readline

while True :
  n = list(map(str, input().rstrip()))
  if len(n) == 1 :           ## 수정했지만 실패!! 
    break
    
  if len(n) % 2 != 0 :
    ls = list(reversed(n))
    print(ls)
    if n == ls :
      print('yes')
  else : 
    print('no')
      

## 예외 [1,1,1,1] 의 경우 리스트의 길이가 짝수이지만 앞 뒤가 똑같다..! 
# 리스트의 길이 상관없이  reverse를 적용했을경우만 비교 

# 통과!


import sys

input = sys.stdin.readline

while True :
  n = list(map(str, input().rstrip()))
  if n == ["0"] :
    break
    
  ls = list(reversed(n))
  
  if n == ls :
      print('yes')
  else : 
    print('no')
      


      
