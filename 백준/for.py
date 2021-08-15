
##8393 

a = int(input())
sum = 0
for i in range(a+1):
    sum = sum + i
print(sum)


##2742 

n = int(input())

for i in reversed(range(1,n+1)):   #reversed 뒤집어서 출력
  print(i)

  
## 11022

n = int(input())

for i in range(1,n+1) : 
  a,b = map(int,input().split())
  print(f"Case #{i}: {a} + {b} = {a+b}")
  
  
## 2438

n = int(input())

for i in range(1,n+1) : 
  print("*"*i)    #문자열과 숫자열 연산가능 
  

## 2439

n = int(input())

for i in range(n):
  a = "*"*(i+n)
  print(a.rjust(n)) # n값에 따라 배열지점 달라짐
 
#
