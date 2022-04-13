
# 어린이 A, 어린이 B 번갈아가면서 입력

n = int(input())  # 라운드 수

for _ in range(n) :
  A = list(input().split())
  A.pop(0)   # 첫번째 값은 딱지의 수 이므로 제거
  
  for _ in range(1) :
    B = list(input().split())
    B.pop(0)

# 리스트를 비교해서 더 큰값을 가지고 있는 리스트를 출력하는 방법? 
# collection? set..? 


# 검색

from collections import defaultdict

number_of_round = int(input())
for round_num in range(number_of_round):
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
  
    A.pop(0)
    B.pop(0)
    
    #각 모양의 개수를 판단하기 위한 딕셔너리 생성
    A_dic, B_dic = defaultdict(int), defaultdict(int)   # 기본값으로 int를 생성
    for num in A:
        A_dic[num] += 1
    for num in B:
        B_dic[num] += 1
    
    #같은 모양 기준, 개수가 더 많은 쪽을 프린트
    #전부 다 같으면 D
    for shape in range(4,0,-1):
        if A_dic[shape] > B_dic[shape] :
            print('A')
            break
        elif A_dic[shape] < B_dic[shape] :
            print('B')
            break
    else :
      print('D')
      

# defaultdict는 key에 대응하는 value가 없을 경우 인자에 들어가는 값이 key에 대응하는 기본값이 된다.  

