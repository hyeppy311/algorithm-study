

import math
T = int(input())

for _ in range(T) :
  x,y = map(int, input().split())

  print(math.lcm(x,y),math.gcd(x,y))
  
  
