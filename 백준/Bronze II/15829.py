

import math

n = int(input())
letter = input()

tmp =[]
for i in range(0,n) :
  tmp.append((ord(letter[i])-96) * math.pow(31,i))

print(int(sum(tmp)))




