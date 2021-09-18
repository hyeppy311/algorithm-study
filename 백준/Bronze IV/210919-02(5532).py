
l,a,b,c,d = [int(input()) for _ in range(5)]


if a//c > b//d :
  if a%c == 0 :
    print(l-a//c)
  else :
    print(l-(a//c +1))

elif a//c == b//d :
  if a%c == 0 and b%d == 0 :
    print(l-a//c)
  else :
    print(l-(a//c +1))

else :
  if b%d == 0 :
    print(l-b//d)
  else :
    print(l- (b//d +1))
    
    
 ## 짧은코드

import math

l,a,b,c,d = [int(input()) for _ in range(5)]

print(l-max(math.ceil(a/c),math.ceil(b/d))) ## ceil : 나머지 올림

