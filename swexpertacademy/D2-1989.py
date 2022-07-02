T = int(input())

for t in range(1,T+1) :
  word = list(input().rstrip())
  palin = list(reversed(word))
  
  
  if word == palin :
    print(f'#{t} {1}')
  else : 
    print(f'#{t} {0}')
          

      
T = int(input())

for t in range(1,T+1) :
  word = input().strip()

  if word == word[::-1].strip() :
    print(1)
  else: 
    print(0)
