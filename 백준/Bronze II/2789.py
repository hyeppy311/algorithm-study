
# 2번째 실패...!! 

word = set(list(input()))

letter = 'CAMBRIDGE'
ans = []

for i in word :
  if i not in letter :
    ans.append(i)
  else:
    pass

print(''.join(ans))


#  set 삭제후 통과 
