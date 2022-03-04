# 생각한 것
# 리스트[0], 리스트[1] 비교하여 같으면 변수에 +=1,  
#                         다르면 [1],[2] 비교  



n = int(input())
ls = [map(int, input().split())]


ans = 0

for i in range(1,n):
    
  if ls[i-1] == ls[i] :
    ans +=1 
  else :
    continue

print(ans) 

# 런타임 에러(index error)남 


# 다른 사람 풀이
n = int(input())
arr = list(map(int, input().split()))
check = [False] * 101      # 100개의 Flase 값을 가진 리스트 생성
 
cnt = 0
for i in arr:             # 입력받은 좌석번호를 하나씩 확인
    if check[i]:          # Flase 리스트에 True가 있으면 변수에 1 더하고
        cnt +=1
    else:                 # 아닐경우(맨 처음)에 True 바꿔줌 
        check[i] = True
print(cnt)


# 비슷한 코드

N = int(input())
PC_Georgia = list(map(int, input().split()))        
PC_checkmate = [0] * 101 #PC방 자리
PC_refused = 0 #거절당한 사람

for i in PC_Georgia:
    if PC_checkmate[i] != 0:     # 입력받은 자리에 0이 아니면 (있다면 else에서 1이 됨)
        PC_refused += 1          # 1을 더해주고 
    else:
        PC_checkmate[i] += 1     # 입력받은 자리에 1로 바꿔줌 

print(PC_refused)


# 함수쓴 코드

N=int(input())
seats=list(map(int, input().split()))
s=len(list(set(seats)))   ## set 함수를 써서 중복값을 리스트에 담아 길이를 계산 ex) 1,2,3,4,4 -> 1,2,3,4로 바꿔줌
print(N-s)                ## 전체에서 set 리스트 길이 빼줌




