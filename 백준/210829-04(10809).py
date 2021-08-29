## 문제) 입력값의 알파벳이 등장하는 인덱스 표시 


import string   

n = list(input())

letter = list(string.ascii_lowercase)     ## a~z까지 리스트에 담기. 

a = [-1]*26                               ## -1로된 리스트 만들기

for idx,i in enumerate(letter):          ## enumerate : 들어온 인자의 인덱스와 원소에 차례대로 접근
  try:
    a[idx] = n.index(i)                 ## 리스트 a에 입력단어 인덱스값 할당
  except:
    pass

for i in a:                             ## 리스트 a 원소출력
  print(i, end=' ')
  
  
