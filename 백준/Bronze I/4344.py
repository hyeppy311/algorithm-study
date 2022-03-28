


c = int(input())


for _ in range(c) :
  scores = list(map(int, input().split()))
  avg = sum(scores[1:]) /scores[0] 

  tmp = []
  for i in scores :
    if i > avg :
      tmp.append(i)
  
  print(f'{(len(tmp)/scores[0])*100:.3f}%')
