
# 내가 생각한 것 
# 맨 처음의 값과 두 번째 값을 비교하여 두번째-첫번째가 양수면 두번째와 세번째의 비교로 넘어감(오르막길)
# 세번째 값과 두번째 값의 차가 양수면 첫번째 값과 세번째 값의 차를 리스트에 저장 
# 


# 검색

from sys import stdin
input = stdin.readline

N = int(input())
A = list(map(int, input().split()))
maxGap = 0
for i in range(N):                  # 여기 for문의 역할은 무엇인지? -> 리스트의 값을 앞 뒤로 비교할라고?
    for j in range(i+1, N):         # 여기 for문의 역할은 무엇인지? 
        if A[j-1] < A[j]:           # 왼쪽과 오른쪽의 값을 비교하여 참이면 
            maxGap = max(maxGap, A[j]-A[i])   # 리스트를 읽으면서 숫자가 증가하면 제일 작은 수와 제일 큰 수의 차를 저장하고 최대값을 계속 또 저장 
        else:                       # 성립하지 않는 경우 if문 빠져나와서 16라인의 for문으로 가서 A[i]의 값 설정 
            break
print(maxGap)


