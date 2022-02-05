
# 삼각수의 수열을 리스트에 저장하여 숫자 3개의 합이 입력값과 같은지 확인


from itertools import combinations

k = int(input())
t = [int(input()) for _ in range(k)]

tmp = []
for i in range(1,44) :
  tmp.append((i*(i+1))/2)

for j in t :
  if j ==  itertools.combinations(tmp, 3) :

## combinations을 사용할 경우 리스트안에 조합이 나오는데 그것을 어떻게 확인한담...? 
## 리스트안에 있는 조합을 다시 빈 리트스에 넣고 tmp와 비교하여 확인..? 
## 너무 복잡함..


# 검색

triangle = [n*(n+1)//2 for n in range(1, 46)]   ## 삼각수열 리스트안에 만들어넣기 
eureka = [0] * 1001                             ## 값이 모두 0인 리스트 만들기 (1,0으로 합 가능 여부 판단) 

#미리 1000이하의 모든 유레카 수를 구한다
for i in triangle:
    for j in triangle:
        for k in triangle:
            if i+j+k <= 1000:                ## 세개의 수를 모두 더해서 1000이하면 
                eureka[i+j+k] = 1            ## eureka의 [i+j+k]자리에 1을 넣는다 -> 왜지? 

T = int(input())
for _ in range(T):
    print(eureka[int(input())])
