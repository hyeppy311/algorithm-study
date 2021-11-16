


n,w,h = map(int, input().split())

M = max(w,h)
m = min(w,h)
for _ in range(n) :
  stick = int(input())

  if stick <= m or stick ** 2 <= (M**2+m**2) :
    print("DA")
  else :
    print("NE")
