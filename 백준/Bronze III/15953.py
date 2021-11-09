
''' 
1. 딕셔너리 만들기 
2. value 값을 차례대로 빼기
3. 음수가 되는 부분의 해당 key값을 리스트에 저장
4. key값 더하기

'''


t = int(input())

def prize_17(n) :
  if n == 1:
    return 5000000
  elif n>1 and n<4 :
    return 3000000
  elif n>3 and n<7 :
    return 2000000
  elif n>6 and n<11 :
    return 500000
  elif n>10 and n<16 :
    return 300000
  elif n>15 and n<22 :
    return 100000
  else :
    return 0
  
def prize_18(n) :
  if n==1 :
    return 5120000
  elif n>1 and n<4 :
    return 2560000
  elif n>3 and n<8 :
    return 1280000
  elif n>7 and n<16 :
    return 640000
  elif n>15 and n<32 :
    return 320000
  else :
    return 0
  
for i in range(t):
  a,b = map(int, input().split())
  print(prize_17(a) + prize_18(b))
  
  ## 그냥 단순하게 등수에 맞게 상금받을 수 있는 인원 잘라서 해주면 됨... 
  ## 본선 진출했어도 등수에 들지 못하거나 입력값이 0이면 받을 수 없음
  
            
            
