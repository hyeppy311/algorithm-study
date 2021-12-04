n = int(input())

for _ in range(n) :
  ls = list(input())

  score = 0               # 안쪽 for문에 적용되는것, 안에다 써줘야함 
  score_sum = 0

  for i in ls : 
    if i == 'O' :
      score +=1 
      score_sum += score
    else : 
      score = 0
    
  print(score_sum)
