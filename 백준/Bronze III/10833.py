n = int(input())

remain = []
for _ in range(n) :
  s,a = map(int, input().split())
  remain.append(a % s)

print(sum(remain))
