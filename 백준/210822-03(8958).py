
n = int(input())

for _ in range(n):
  a = input()
  
  correct_num = 0
  total_score = 0
  
  for i in a :
    if i == 'O' :
      correct_num += 1               ## count 찾아보기 
      total_score += correct_num
    else :
      correct_num = 0  
  
  print(total_score)

