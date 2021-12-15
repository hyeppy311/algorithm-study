

n = list(input())
print(n)

height = 0

for i in n :
  if i == '(':
    height += 5
  elif i == ')' : 
    height += 10 
  
print(height+5)


## 처음 오는 그릇의 모양과 그 다음의 모양을 판단 하는 코드를 짜야함 
# 1. (( 일 경우
# 2. () 일 경우
# 3. )) 일 경우
# 4. )( 일 경우

for i in range(len(n)) :
  if n[i] == n[i+1] :           ## 인덱스 범위 넘어가버림
    height += 5
  else : 
    height += 10    


# range 범위 줄이기

for i in range(0,len(n)-1) :
  if n[i] == n[i+1] :
    height += 5
  else : 
    height += 10

print(height)


## 정답!! 

n = list(input())
height = 10                   ## 처음 그릇의 높이 10에서
  
for i in range(0,len(n)-1) :
  if n[i] == n[i+1] :         ## 그릇 모양이 같으면 (( +5
    height += 5
  else :                      ## 다르면 () +10
    height += 10

print(height)
