
# 어떤 수 n을 제외한 모든 약수들의 합과 n이 같을 경우 /  아닌 경우 출력


# 시도 
while True : 
  n = int(input())
  if n == -1 :
    break

  tmp = []
  for i in range(1,n+1) :      # n을 포함시키지 않는게 다음 조건문에서 코드가 더 보기좋아짐
    if n % i == 0 :
      tmp.append(i)
      
  if sum(tmp)-n == n :          # sum(tmp) == n 
    for i in tmp :
      print(n = i + '+')      # 출력 6 = 1 + 2 + 3 이렇게 어떻게 해야할까? 
  else :
    print(n,"is NOT perfect.")
    
 

## 검색

while True:
    n = int(input())
    if n == -1: # 입력 값이 -1이면 반복문 종료
        break;
    arr = []
    for i in range(1, n):
        if n % i == 0:
            arr.append(i)
    if sum(arr) == n:
        print(n, " = ", " + ".join(str(i) for i in arr), sep="")   # str.join(iterable) # 띄어쓰기 유의
    else:                                                          # f-string : print(f"{n} = {' + '.join(str(i) for i in arr)}")
        print(n, "is NOT perfect.")
        

