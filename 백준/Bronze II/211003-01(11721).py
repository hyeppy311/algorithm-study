

## 긴 코드

words = list(input())

start = 0
end = len(words)
div = 10

for i in range(start, end+div, div) :
  out = words[start:start+div]
  if out !=[]:
    print(*out,sep='')
  start =  start+div
  
  
  
  ## 짧은 코드 
  
words = input()

for i in range(0,len(words),10) :         ## 0부터 word 길이까지 10 단위로 ,,, (0,10,20,30 ...)
  print(words[i: i+10])
