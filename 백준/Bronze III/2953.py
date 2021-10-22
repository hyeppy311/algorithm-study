

score = [list(map(int, input().split())) for _ in range(5)]

total = []

for i in range(5) :
  total.append(sum(score[i]))

tmp = max(total)
index = total.index(tmp)

print(index+1, tmp)
