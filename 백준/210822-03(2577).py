
a = int(input())
b = int(input())
c = int(input())

m = str(a*b*c)

print(m.count('0'))    ## 반복인데..얘를..짧게 어떻게 나타내짐..? for문? 
print(m.count('1'))
print(m.count('2'))
print(m.count('3'))
print(m.count('4'))
print(m.count('5'))
print(m.count('6'))
print(m.count('7'))
print(m.count('8'))
print(m.count('9'))


## 시도했지만 실패 

for i in range(10) : 
  print(m.count('i'))   # 문자열로 바꿔줬는데 왜안됨..?

## 짧은 코드 

for i in range(10)
  print(m.count(str(i)))
