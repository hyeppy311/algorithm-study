

N = int(input())

nums = ["3","6","9"]

for i in range(1,N+1) :      
  cnt = 0
  for j in str(i) :    # 숫자를 문자열로 변환해서 하나씩 확인
    if j in nums :     # 3,6,9를 확인하면서 cnt 올려주고
      cnt += 1

  if cnt > 0 :        # cnt가 0 이상 이면
    i = "-" * cnt     # "-" 를 3,6,9 개수에 맞게 올려줌

  print(i, end=" ")   # 출력
      
  
  # 숫자 -> 문자열로 바꿔주기
  # for문으로 문자열 하나씩 확인 
