
# 모든 행과 열에 한 명 이상의 경비원 


# 시도
# 행,열 다 비어있더라도 행이나 열 둘 중 한곳에만 있어도 조건에 만족해서 행 탐색 -> 가로가 비어있더라고 세로가 비어있을 경우 가 있음
# 예시
'''
....XXXX
........
XX.X.XX.
........
........

'''
# 답은 나오는데 제출은 틀렸음

n,m = map(int, input().split())
castle = [list(input()) for _ in range(n)]    # 수정 [input() for _ range(n)]

guard = 0 

for i in castle :
  if "X" in i :        # 없는 경우 +1 하는것이 코드가 더 간결함
    pass
  else : 
    guard += 1

# 모든 행과 열의 최소 경비원 수에서 빼야할까? 

# 검색
# 가로, 세로 모두 탐색해줘야 함 

n, m = map(int,input().split())
board = []

for _ in range(n):
    board.append(input())      # ['XX...', '.XX..', '...XX'] 굳이 2차원으로 나누지 않아도 됨 

a, b = 0, 0                    # 가로, 세로 따로 변수 설정

for i in range(n):
    if "X" not in board[i]:     # 가로에 없으면 +1 
        a += 1

for j in range(m):
    if "X" not in [board[i][j] for i in range(n)]:   # 슬라이싱해서 세로 리스트를 만들어줌. j = 0 일 때 i = 0,1,2..로 변함 
        b += 1

print(max(a ,b))       # 둘 중 더 큰 값 출력 (가로,세로 다 비어있을 경우 최소값을 선택시 다른 곳에 공백이 생김)


# 문자열도 슬라이싱이 가능한 것 잊어버리지 말기.!! 
# 라인 47 세로 값을 담는 코드 잘 기억하기 
# 조건문에서 반대 경우 not으로 표현 

