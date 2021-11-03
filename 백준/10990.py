

n = int(input())
print(" "*(n-1) + "*")            ## 맨 처음 별 하나 찍고

for i in range(n-1) : 
  print(" "*(n-2-i) + "*" + " "*(2*i+1) + "*" )     ## 공백 + 별 + 공백 + 별
