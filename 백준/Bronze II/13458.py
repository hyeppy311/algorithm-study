

# n개의 시험장. i번 시험장 응시자수 Ai명.

# 총감독관 감시응시자 B명
# 부감독관 감시응시자 C명

# 각 시험장 총감독 1명 부감독 여러명가능 

# 응시생 모두 감시, 필요한 감독관의 최솟값 



n = int(input())  # 시험장의 개수 

for i in range(n) :
  a = list(map(int,input().split()))  # 응시자의 수 

b, c = map(int, input().split())
