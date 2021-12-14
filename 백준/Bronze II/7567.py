

n = list(input())
print(n)

height = 0

for i in n :
  if i == '(':
    height += 5
  elif i == ')' : 
    height += 10 
  
print(height+5)
