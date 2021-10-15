
n,m = map(int, input().split())

if m <= n and m not in [1,2] :
  print("OLDBIE!")
elif m in [1,2] :
  print("NEWBIE!")
else:
  print("TLE!")
  
  ## 문자열 출력 조심! 스펠링 확인!! 
  
  
  ## 짧은 코드 
  
  if m <= 2 : print("NEWBIE!")
  elif m<=n : print("OLDBIE!")
  else : print("TLE!")
