
# 플레이어는 카드에 숫자를 적는다
# 다른 사람과 숫자가 겹치지 않으면 숫자와 같은 점수 획득
# 같은 사람이 있을 경우 점수 얻을 수 없음
# 게임은 3번 진행됨

# 입력으로 참가자의 수 n과 n개의 줄에는 1,2,3번째 게임에서 쓴 숫자

# 2차원 리스트로 풀어야 할까..? 
# 입력으로 들어온 값의 행끼리 비교해야되는데... 


# 검색 
n = int(input())
score = [[], [], []]               # 점수를 저장할 빈 리스트 생성 
sum = []                           # 점수계산 리스트 

for i in range(n):
    a, b, c = map(int, input().split())     # 숫자 3개를 나눠서
    score[0].append(a)                      # 점수 리스트에 각 게임별로 넣어줌
    score[1].append(b)
    score[2].append(c)

for i in range(n):                          # score 리스트 [[100, 100, 63, 99, 89], [99, 97, 89, 99, 97], [98, 92, 63, 99, 98]]
    s_score = 0                                               # 1번째 게임              2번째 게임                3번째 게임
    for j in range(3):
        if score[j].count(score[j][i]) == 1:    # 각 게임에서 점수가 1개이면 
            s_score += score[j][i]              # 그 점수를 합해준다
    sum.append(s_score)                         # sum 리스트에 추가

for i in sum:                                # 플레이어의 점수 합계 출력 
    print(i)

# 처음 코드를 짤 때 2차원 리스트로 받아서 각 게임별로 어떻게 처리해야할지 헷갈렸음

# 2차원 리스트로 입력받은 검색 코드

N = int(input())
li = [list(map(int, input().split())) for _ in range(N)]   
# li = [[100, 99, 98],
#       [100, 97 ,92],
#       [63 ,89 ,63],
#       [99, 99, 99],
#       [89, 97 ,98],
#       ]

for i in range(N):
    s = 0
    for j in range(3):
        t = li[i][j]                 # 플레이어의 점수를 t에 저장. (행으로 탐색하여 저장)
        ok = 1
        for k in range(N):           # 게임 참가의 수 만틈 for문 수행
            if k == i:               
                continue
            if li[k][j] == t:        # 행 탐색으로 저장했던 t를 열로 내려오면서 비교 (100을 100->100->63->99->89 순서로 비교)
                ok = 0; break        # 같으면 ok를 0으로 만들고 멈춤, 다음 계속 비교 
        if ok == 1:
            s += t
    print(s)
 
# 처음에 구현하려고 했던 코드와 제일 비슷한데 ok의 역할은 뭘까..? 
# for문과 if문을 섞어서 구현하는게 아직 어려움 
