n = int(input())

answer = 0

for _ in range(n) :
  
  letter = input()
  temp = str()
  st = set()

  for i in letter :
    if i not in st :
      st = st | {i}
      temp = i 
    elif i == temp :
      pass
    else : 
      st = False 
      break
  if st :
    answer += 1

print(answer)


