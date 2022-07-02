ans = []
for i in range(5) :
  score = int(input())

  if score < 40 : 
    score = 40 
    ans.append(score)

  else : 
    ans.append(score)

print(sum(ans)//5)

