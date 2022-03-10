

n = int(input())
scores = list(map(int, input().split()))

score = []
for i in scores :
  score.append(i/max(scores)*100)

print(sum(score)/len(score))


