
## 시도한 코드 


n = int(input())

for _ in range(n) :
  times, letter = input().split()

  for i in letter :
    print(i * int(times), end = '')
   
  ## print() 줄바꿈 추가 해줘야함...
    
    
 ## 이전에 제출한 코드 

n = int(input())

for _ in range(n) : 
  a,b = input().split()
  a = int(a)

  for i in b : 
    print(i*a, end = '')
  print() 

  
  ## 다른코드
  
n = int(input())

for _ in range(n) :
  times, letter = input().split()
  temp = " "

  for i in letter :
    temp += i * int(times)   # 빈 문자열에 원소 하나씩 곱해서 추가
  print(temp)

  
  
