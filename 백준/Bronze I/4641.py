
# 리스트 원소가 리스트 안에서 자신의 2배인 수의 개수

# 입력 조건 
# 여러개의 테스트 케이스 , 입력 끝에는 -1  : while 문으로 처리
# 리스트 끝은 0으로 판별 (리스트에 속하지 않음) : pop() 이용

# 시도 
while True :
  nums = list(map(int, input().split()))
  if len(nums) == 1:
    break
  nums.pop()
  
  cnt = 0 
  for i in nums :
    if (i // (i // 2)) == 2:
      cnt += 1
  print(cnt)
  
# 맨 마지막 원소 0을 꺼냈는데 왜 ZeroDivisionError가 나는 걸까...? 

# 문제를 잘 못 이해했다..

# 검색 

while True :
  nums = list(map(int, input().split()))
  if len(nums) == 1:
    break
  
  cnt = 0 
  for i in range(len(nums)-1) :     # 0 제외
    if nums[i] * 2 in nums :
      cnt += 1
  print(cnt)
  
  
