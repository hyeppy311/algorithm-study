h,m = map(int, input().split())

a = m-45  # 분으로 판단하기 위해 변수 지정 

if a < 0 :         # 분이 음수일경우   
  if h == 0 :      # 입력값이 0:00 ~ 0:45일 경우 출력
    print(23, m+15)  
  else :            
    print(h-1 , m+15) 
    
elif a >= 0 :  # 분이 양수일경우 
 print(h, a)   # 시,분 그대로 출력 
