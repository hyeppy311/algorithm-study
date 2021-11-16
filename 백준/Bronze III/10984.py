
T = int(input())

for _ in range(T) :
  n = int(input())

  grade = score = 0

  for _ in range(n) :
    c,g = map(float, input().split())

    grade += c
    score += c * g

  print(int(grade), round(score/grade,1))


