

T = int(input())      ## 테스트 케이스의 갯수

for _ in range(T) :   
  
  n =  int(input())        ## 자연수의 갯수
  nums = sum(list(map(int, input().split())))  ## n개의 자연수
  print(nums)
  
  
  
  ## 자연수의 갯수와 n개의 자연수가 T만큼 들어온다.
  ## 단순하게 따로따로 변수로 지정해서 for문 돌려주면 된다. 
  
