


n = input()

lst = [0] * 26 

abc = 'abcdefghijklmnopqrstuvwxyz'

for i in n :                    ## 입력값을 하나씩 탐색 
  if i in abc :                 ## abc 문자열의 인덱스 찾기
    idx = abc.index(i)
    lst[idx] +=1 

print(*lst)
