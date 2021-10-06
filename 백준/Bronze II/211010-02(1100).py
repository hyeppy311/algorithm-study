## 처음 코드 

for _ in range(8) :               ## 입력 틀림 
    chess = list(input())
   

temp = []

for i in range(0,8) :
    for j in range(0,8) :
        if i % 2 == 0 and j % 2 == 0 :            ## 하얀 칸이 되는 조건은 있지만 하얀 칸이 F라는 조건이 없음 
           temp.append(chess[i][j])
        elif i % 2 ==  1 and  j % 2 == 1 :
           temp.append(chess[i][j])

print(sum(temp))

## 하얀 칸을 list에 담아서 F의 갯수를 세고 싶었는데 실패함.. 
## 위 코드는 하얀 칸만 리스트에 담음 , 그럼 또 리스트 내에서 F가 있는지 확인해야함 
## 근데 아무 조건도 없이 왜 print 한거지? 
## 그리고 str이라 sum 안되느 에러남... 



## 수정한 코드 (다른사람 코드 참고) 

chess = [input() for _ in range(8)]      

cnt = 0 

for i in range(8) :
    for j in range(8) :
        if i % 2 == 0 and j % 2 == 0 and chess[i][j] == "F" :         
          cnt += 1
        elif i % 2 ==  1 and  j % 2 == 1 and chess[i][j] == "F":
          cnt += 1

print(cnt)


