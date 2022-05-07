n = int(input())
class_num = [list(map(int, input().split())) for _ in range(n)]
same_max = [0]*n


for p_class in zip(*class_num) :
  for idx, val in enumerate(p_class) :
    if p_class.count(val) > 1 :
      same_max[idx] += 1
print(same_max)
ans = 0
for i in range(len(same_max)) :
  if same_max[i] == max(same_max) :
    ans += i
    break
print(ans+1)
