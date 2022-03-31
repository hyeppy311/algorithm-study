
# 범위가 있는 숫자 안에서 완전제곱수를 찾고 그 합과 최소값 구하기
# 어떤 수의 완전제곱임을 알려면 그 수를 제공해야되는데 
# 수를 어떻게 제공해야될지 잘 모르겠다. 

# 수의 범위가 10000까지니 100까지 우선 시도해본다. 



n = int(input())
m = int(input())

ls = [i for i in range(n,m+1)]

tmp = []
for i in range(1,100) :
      if i*i in ls :
            tmp.append(i*i)
      else :                     # 항상 예외처리를 어떻게 해야될지.. 
        print(-1)
            
print(sum(tmp))
print(min(tmp))


# 검색 
# while문을 이용한 방법

m = int(input())
n = int(input())
num = []
i = 1
while i ** 2 <= n:           # 범위가 m <= 완전제곱수 <= n 이므로 n이하의 값을 i를 하나씩 올려주면서 찾음
    if m <= i ** 2 <= n:     # 범위안에 있으면 리스트에 넣어주고
        num.append(i ** 2)
    i += 1
if num == []:                # 리스트가 비어있으면 -1
    print(-1)
else:                        # 아니면 출력 
    print(sum(num))
    print(num[0])
    
    
# 제곱근을 이용한 방법

M = int(input())
N = int(input())
sqrt_list = []
for i in range(M, N+1):         # 주어진 범위에서 
    T = int(i ** 0.5) ** 2      # 제곱근을 해주고 정수형으로 변환 후 다시 제곱 해줌 
    if i == T:
        sqrt_list.append(i)

if sqrt_list:
    print(sum(sqrt_list))
    print(min(sqrt_list))
else:
    print(-1)
    
# 
