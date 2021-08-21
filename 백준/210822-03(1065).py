
n = int(input())

if n < 100 : 
  print(n)
else :
  answer = 99
  for i in range(100,n+1) : 
    s = str(i)
    if int(s[0])+int(s[2]) == 2*int(s[1]) :
      answer += 1

  print(answer)
  
  
  
