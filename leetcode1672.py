# 1672. Richest Customer Wealth

# 1. 리스트 안 리스트의 요소를 다 더한다. 
# 2. 각 리스트 합의 크기를 비교한다.
# 3. 제일 큰 수 출력한다.

accounts = [[1,5],[7,3],[3,5]]  

# 리스트 내 리스트 합 구하기 
therichest = ([sum(i) for i in accounts]) 

  # 질문? 1. accounts 내 리스트가 어떻게 i로 들어가는 것일까? 
  #      2. []가 의미하는 것은? 
  #      3. 대체 함수로 어떻게 만드는거지...?

  
  print (max(therichest))

  
