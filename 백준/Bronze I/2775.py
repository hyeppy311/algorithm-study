# 수열문제
# 0층 1,2,3,4,5,...증가
# 1층 1,3,6,10,..

# 윗층은 밑의 층의 각 호의 사람수만큼 증가 
# 0층의 [1,2,3...14] 까지 리스트를 만들어서 증가시키는 방법...? 


T = int(input())

for _ in range(T) :
  k = int(input()) 
  n = int(input())

ls = [i for i in range(1,15)] 

# 여기까지 작성하고 막혀버림.. 


# 검색 

T = int(input())

for _ in range(T) :
  k = int(input())  #층
  n = int(input())  #호수

  ls = [i for i in range(1,n+1)]  # 0층인 리스트 생성해주고 

  for j in range(k) :         # k층 만큼 반복 (층만들기) 
    for f in range(1,n) :     # 호수에 사람 증가시킴 
      ls[f] += ls[f-1]        # [1,2,3] -> [1,3,6] -> [1,4,10]
  print(ls[-1])               # 맨 마지막(호수) 출력
  
  
  
  
