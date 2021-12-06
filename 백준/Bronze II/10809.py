
## 처음에 생각한 코드 
# 1. -1로 된 리스트 생성
# 2. 입력받으 문자의 인덱스를 1번의 리스트에 치환 
# 3. 출력


## 제일 처음 제출한 코드

import string 

n = list(input())

letter = list(string.ascii_lowercase)       ## 알파벳 순서대로 리스트에 넣어주는 코드

a = [-1]*26                                 ## -1로되 리스트 만들고
  
for idx,i in enumerate(letter):             ## 알파벳 리스트에서 인덱스와 원소를
  try:
    a[idx] = n.index(i)                     # 생성한 리스트에 입력값의 인덱스를 넣어줌
  except:
    pass

for i in a:
  print(i, end=' ')                         # a로 만들어준 리스트의 원소를 for문으로 출력

  

# 다른 사람 코드  

S = input()
abc ='abcdefghijklmnopqrstuvwxyz'

for i in abc:                             # 알파벳의 원소에서   
    if i in S:                            # 입력받은 알파벳이 있으면 
        print(S.index(i), end= ' ')       # 입력값의 인덱스 출력
    else:
        print( -1, end =' ')              # 없으면 -1 


## 내가 생각한것과 반대로 한 코드, 훨씬 간단하다.
## 전체 알파벳을 기준으로 입력받은 알파벳의 위치를 넣어준다. 


## 다른사람코드 2 

letter = input()
ls = list(range(97,123))   ## 아스키코드로 만든 리스트 

for i in ls :
  print(letter.find(chr(i)), end = ' ')    ## find()는 해당값을 돌려주고 없으면 -1을 반환
  
  
  
  
