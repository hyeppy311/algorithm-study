

score = [int(input()) for _ in range(5)]


for idx, value in enumerate(score) :
  if value < 40 :
    score[idx] = 40
    
print(sum(score)//len(score))


