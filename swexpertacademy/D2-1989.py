T = int(input())

for t in range(1,T+1) :
  word = list(input().rstrip())
  palin = list(reversed(word))
  
  
  if word == palin :
    print(f'#{t} {1}')
  else : 
    print(f'#{t} {0}')
          
