
# 시도 -> 답은 나오지만 제출시 틀림

n = int(input())
class_num = [list(map(int, input().split())) for _ in range(n)]
same_max = [0]*n    # 같은 반의 개수


for p_class in zip(*class_num) :
  for idx, val in enumerate(p_class) :   
    if p_class.count(val) > 1 :    # 같은 반이 1개 이상이면 
      same_max[idx] += 1           # 1 올려주고  same_max = [0, 1, 2, 3, 1]

ans = 0
for i in range(len(same_max)) :       # 같은 반의 개수 리스트에서
  if same_max[i] == max(same_max) :     # 같은 반이였던 학생이 있으면
    ans += i                            # 인덱스 담아주고 break
    break
  else : 
    print(same_max.index(max(same_max))+1)    # 같은 반을 했던 학생의 최대값이 여러명이면 인덱스에 1 더해서 출력 
print(ans+1)                            # 인덱스 순서대로 1,2,3,4,5 번 학생이므로 1더해서 출력 


# for문을 안쓰고 바로 라인 18만 해도 되는데..ㅠㅠ 

# 검색

n = int(input())
ban = []
same = [0] * n
for i in range(n) :
  ban.append(list(map(int,input().split())))
  same[i] = [0] * n

for i in range(5) :  # 학년 
  for j in range(n) :  # 다른 번호의 같은 학년을 비교 j번의 i학년
    for k in range(j+1, n) :    # k번의 i학년
      if ban[j][i] == ban[k][i] : # 반이 같으면 
        same[k][j] = 1            # 1로 바꿔주고 
        same[j][k] = 1


cnt = []      
for s in same :
  cnt.append(s.count(1))    # [0, 1, 2, 3, 2] 각 학생이 같은 반을 한 횟수

print(cnt.index(max(cnt))+1)


# 각 학생의 반을 다른 학생의 반이랑 비교하며 카운트 해줘야 하는데 
# 학년별로 모아서 비교를 해서 카운트 수가 달라짐 
