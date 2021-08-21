n = int(input())

for _ in range(n):
  score = list(map(int,input().split()))
  a = score.pop(0)
  
  avg = sum(score)/a

  c = []
  for i in score :
    
    if i > avg :
      c.append(i)
      
  print('{0:0.3f}%'.format(len(c)/len(score)*100)) ##foramt 소수점 나타내기 
