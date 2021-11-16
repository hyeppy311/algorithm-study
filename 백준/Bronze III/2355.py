
## 시도한 코드

a,b = map(int, input().split())

sums = 0

for i in range(a,b+1) :
  sums += i

print(sums)


# 시간초과 뜸..!
# 시간제한 걸려있기 때문에 반복문으로 하면 시간에 걸림쓰.. 


## 검색코드 
## a,b가 무조건 a<b 라는 보장은 없다.
## 두 수를 큰 수와 작은 수로 꼭 구분!! 

A, B = map(int, input().split())

m = max(A, B)
n = min(A, B)
sums = (A + B) * (m - n + 1) / 2   
print(int(sums))


## 단순한 수학식으로 해결
