## 공백없는 A+B

## 1
number = list(input())


if len(number) == 2 :
  print(int(number[0])+int(number[1]))

elif len(number) == 3 :
  print(int(number[0]+number[1]) + int(number[2]))
  
## 예제만 보고 3자리 수 까지만 구함 -> 틀! 



## 2 문제 해석 -> 11부터 1010까지 




## 3 수를 더해서 합해야 하는 수와의 차를 더해주기 

n = list(input())

if len(n) == 2 :
  print(sum(map(int,n)))
elif len(n) == 3 : 
  print(sum(map(int,n))+9)
elif len(n) == 4 :
  print(sum(map(int,n))+18)


