## 공백없는 A+B

## 1
number = list(input())


if len(number) == 2 :
  print(int(number[0])+int(number[1]))

elif len(number) == 3 :
  print(int(number[0]+number[1]) + int(number[2]))
  
## 예제만 보고 3자리 수 까지만 구함 -> 틀! 



## 2    
n = list(input())

if len(n) == 2 :
    print(int(n[0])+int(n[1]))

elif len(n) == 3 : 
  if n[1] == "0" :            #101, 110 나눠주기 
    print(10 + int(n[-1]))
  else :
    print(10 + int(n[0]))
    
else :
  print(20)



## 3 수를 더해서 합해야 하는 수와의 차를 더해주기 

n = list(input())

if len(n) == 2 :
  print(sum(map(int,n)))
elif len(n) == 3 : 
  print(sum(map(int,n))+9)
elif len(n) == 4 :
  print(sum(map(int,n))+18)
  
  
## 짧은 코드

s = input()
if s[1] == '0':                     # 101~ 1010일 경우, 10과 인덱스2부터 끝까지 
    print(10 + int(s[2:]))
else:                               # 그 외 110 ~ 910의 경우 
    print(int(s[0]) + int(s[1:]))   


