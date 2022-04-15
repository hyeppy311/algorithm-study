

# 5개의 숫자 중 3개의 최소공배수를 구하는 것

# math 모듈을 사용했지만 안댐.. 

# 검색
# 5개의 수 중에 가장 작은 수를 하나씩 올리면서 3개로 나눠떨어지는 수를 출력하면 됨 

nums = list(map(int, input().split()))
min_num = min(nums)

while True :
  cnt = 0
  for i in range(5):
    if min_num % nums[i] == 0 :   # 최소값을 5개 수로 나눠주면서 0이 되는 값이 있으면
      cnt += 1                    # 카운트 해주고 
  if cnt > 2 :                    # cnt의 값이 2 이상이면 
    print(min_num)                # 최소값 출력(배수)
    break
  min_num +=1                     # 최소값에 1씩 더해줌
  
  
  
  # 15~17 라인 -> 18라인 ~  -> 21라인 
