

nums = [int(input()) for _ in range(9)] 


tmp = []

for i in nums[0:9] :              # 리스트 처음부터 끝까지
  for j in nums[1:9] :            # 2번째부터 끝까지 
    if i+j == sum(nums) - 100 :   # 입력값을 다 합한 것에서 100을 빼고 합한 수 
      tmp.append(i)               # 각 각 하나씩 담고 
      tmp.append(j)

print(tmp[0:2])



from itertools import combinations        ## 조합 

nums = [int(input()) for _ in range(9)] 
comb = list(combinations(nums,7))      ## 9개의 원소에서 7개 추출

for i in comb :                       # 그 조합들에서 합이 100이 되는 숫자들 출력
  if sum(i) == 100 :
    print(*i,sep='\n')
