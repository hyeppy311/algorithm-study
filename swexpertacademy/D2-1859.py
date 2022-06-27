# N일 동안 매매가 제공 
# 마지막 날 판매하여 이익구하기 

# 약간 주식느낌으로 문제를 이해하면 됨 

# 처음에 문제가 이해 잘 안되서 코드 검색 

T = int(input())              # 테스트 케이스

for t in range(1, T+1) :      
  N = int(input())           # N일 
  price = list(map(int, input().split()))   # N일동안 N개의 매매가 
  
  max_val = price[-1]      # 풀이핵심 -> 맨 마지막 가격을 최대값으로 설정하여 전 날로 이동하면서 비교 
  profit = 0               # 이익변수 선언

  
  for i in range(len(price)-2, -1, -1) :    # N-2 날 부터 전 날로 이동하는 for문 
    if price[i] >= max_val :                # 현재값이 최대값보다 크거나 같으면
      max_val = price[i]                    # 최대값을 현재의 값으로 초기화
    else : 
      profit += max_val - price[i]          # 아닐경우 최대값에서 현재의 값의 차(이익)을 이익변수에 넣어줌

  print("#{} {}".format(t,profit))          # 출력 
  
  

