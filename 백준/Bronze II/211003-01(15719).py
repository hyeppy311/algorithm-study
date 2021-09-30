

n = int(input())

for _ in range(n) :
  a_ls = list(map(int, input().split()))

  # ls = []
  # for i, val_1 in enumerate(len(a_ls)) :    
  #   for j, val_2 in enumerate(n+1) :   ## list index 범위 초과 -> 다시생각해보자
  #     if val_1 == val_2 :
  #       ls.append(i)

  # print(ls[i])

  ls = []
  for i in range(len(a_ls)-1) :
    a_1 = a_ls[i]
    a_2 = a_ls[i+1]
    
    if a_1 == a_2 :
      ls.append(a_1)

  print(*ls)
