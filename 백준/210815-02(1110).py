n = input()        ## 입,출력은 str 타입임

if len(n) == 1 :   ## 입력값이 한 자릿수 일 경우
  n = '0'+ n       ## 앞에 0을 붙여줌

a = int(n[0])     ## string indexing. 
b = int(n[1])

cycle = 0

while True: 
  
  sums = (a+b)%10   ## 나머지 -> 일의 자리 수
  a,b = b,sums      ## 다시 a에 b(일의자리수), b에 sums(합한값) 할당 
                    
  cycle = cycle + 1   ## 14,15라인 계속 돌고

  if (n == 10*a+b):   ## a를 10의자리 수로 만들어서 b를 더해주고 처음 입력값이랑 같으면
    print(cycle)      ## 출력하고 
    break             ## 멈춤
