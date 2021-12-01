

a,b,c = (int(input()) for _ in range(3))

multi = list(str(a*b*c))

z = 0
one = 0 
two = 0
three = 0
four = 0
five = 0
six = 0
seven = 0 
eight =0 
nine = 0

for i in multi :
  if i == "0" :
    z+=1 
  if i == "1" :
    one+=1 
  if i == "2" :
    two+=1
  if i == "3" :
    three+=1
  if i == "4" :
    four+=1
  if i == "5":
    five+=1
  if i == "6":
    six+=1
  if i == "7":
    seven+=1
  if i == "8":
    eight+=1
  if i == "9":
    nine+=1

print(z,
one,
two,
three,
four ,
five ,
six ,
seven , 
eight , 
nine , sep='\n')

## 처음제출에서는 srt.count()를 썼음 

## 짧은 코드 검색 

answer = 1
for _ in range(3):
  answer *= int(input())   # 입력받으면서 곱해주기 
lst = [0] * 10             # 0으로 된 리스트 만들어주기 
for i in str(answer):      # 입력받은 숫자를 문자로 변환 for문으로 돌리고
  lst[int(i)] += 1         # 0부터 개수 출력이므로 인덱스에 맞게 숫자 카운트  
for i in lst:
  print(i)                 # 개수 넣어준 리스트 출력
  
----------------------------------------------------------------------
# 이것은 내가 푼것같은뎁..? 

a = int(input())
b = int(input())
c = int(input())

m = str(a*b*c)

for i in range(10) :
    print(m.count(str(i)))
    


  


