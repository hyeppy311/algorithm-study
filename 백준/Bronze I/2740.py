
# 행렬곱셈

# numpy로 시도하려고 했으나 int가 콤마로 구분되어있지 않음
# 콤마 삽입 어떻게? 

# 아니면 for문으로 슬라이싱해서 하나씩 곱해줘야함..? 

# 행렬은 M*N , N*K 가 있을 때 M*K의 형태로 만든다 

# 작성코드


n,m = map(int,input().split())
a = [list(map(int, input().split())) for _ in range(n)]

m,k = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(m)]

# 입력까지밖에 못함

# 검색

n, m = map(int,input().split())
A = [list(map(int,input().split())) for i in range(n)]
m, k = map(int,input().split())
B = [list(map(int,input().split())) for i in range(m)]

for i in range(n):        
    result = []
    for l in range(k):
        a = 0
        for j in range(m):           
            a += A[i][j] * B[j][l]
        result.append(a)
    print(*result)
