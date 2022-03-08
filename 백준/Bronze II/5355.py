## 첫번째 시도
# 계신 후 값을 가져오는 변수 설정에서 계속 막힘

t = int(input())

for _ in range(t):
    lst = list(input().split())
    num = float(lst[0])
    ans = 0                             ## 변수설정을 할 필요 없이 바로 num에 계산해주면 됐음
    for i in range(1, len(lst)):
        if lst[i] == "@":
            ans += num * 3
        elif lst[i] == "%":
            ans +=  5
        else :
            ans -= 7
        
    print(f'{ans : .2f}')



# 검색

case = int(input())

for _ in range(case):
    mars = list(map(str, input().split()))
    answer = 0
    
    for i in range(len(mars)):          ## 리스트길이만큼 for문 반복하고
        if i == 0:                      # 리스트 맨 앞이 숫자니깐 변수에 넣어주고 
            answer += float(mars[i])
        else:                           # i가 1부터 문자 판별해서 연산해줌
            if mars[i] == "#":
                answer -= 7
            elif mars[i] == "%":
                answer += 5
            elif mars[i] == "@":
                answer *= 3
                
    print("%0.2f" % answer)
    

 # 검색 2

T = int(input())

for i in range(T) :
  lst = input().split()
  num = float(lst[0])
  opers = lst[1:]                 ## 처음 내 코드에서 변수 = 0을 따로 할 필요가 없었음 
  
  for oper in opers :
    if oper == "@" :
      num *= 3 
    elif oper == "%" : 
      num += 5 
    else :
      num -= 7
  print(format(num,".2f"))

  
