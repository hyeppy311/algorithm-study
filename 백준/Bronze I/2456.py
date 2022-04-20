
# 1,2,3 각 학생의 점수를 딕셔너리로 받음

from collections import defaultdict
n = int(input())

dic = defaultdict(list)

for _ in range(n) :
  a,b,c = map(int, input().split())

  dic[1].append(a)
  dic[2].append(b)
  dic[3].append(c)



# 점수의 최대값과 3,2,1의 최대 개수를 변수에 저장 

max_num = max(sum(i) for i in list(dic.values()))
max_3= max([i.count(3) for i in list(dic.values())])
max_2= max([i.count(2) for i in list(dic.values())])
max_1 = max([i.count(2) for i in list(dic.values())])

# 최대값과 3,2,1 최대 개수를 비교, 학생 번호와 점수의 합 출력 
for k,v in dic.items() :
  if v.count(3) == max_3 and v.count(2) == max_2 and v.count(1) == max_1 :   # 3,2,1의 개수가 모두 같을 경우 
    print(0,sum(v))
    break
      
  elif sum(v) == max_num and v.count(3) == max_3:    # 3의 개수가 제일 큰 경우
    print(k,sum(v))
    break
  elif sum(v) == max_num and v.count(2) == max_2 :   # 2의 개수가 제일 큰 경우 
    print(k,sum(v))
    break

# 검색
# 학생이 받은 점수를 제곱하여 비교한다. 

import sys
input = sys.stdin.readline

n = int(input())

ls = [0] * 3
ls_pow = [0] * 3

for _ in range(n) :
  a,b,c = map(int, input().split())

  ls[0] += a
  ls[1] += b
  ls[2] += c

  ls_pow[0] += (a * a)
  ls_pow[1] += (b * b)
  ls_pow[2] += (c * c)

max_score = max(ls)                # 점수 중 제일 큰 값 변수에 담아주고
if ls.count(max_score) == 1 :      # 1명이면 
  for i in range(len(ls)) :        
    if ls[i] == max_score :
      print(i+1, max_score)        # 번호와 제일 큰 점수 출력
      break;
else :                              # 아닐경우
  pow_max_score = max(ls_pow)       # 점수를 제곱한 수 중 제일 큰수를 담아주고
  idx= ls_pow.index(pow_max_score)        # 제일 큰 값의 인덱스 변수 설정
  if ls_pow.count(pow_max_score) == 1:    # 제일 큰 값이 1명이명 
    print(idx+1,ls[idx])                  # 번호와 제일 큰 점수 출력
  else: 
    print(0,ls[idx])
    
# 점수가 같을 경우 3점이 제일 많은 경우, (3점이 같은 경우) 2점의 개수가 많은 사람이 선출 
# 3,2,1의 개수를 따질 필요 없이 제곱해서 제일 큰 수를 가진 번호와 값을 출력해 주면됨 


