import string 

n = list(input())

letter = list(string.ascii_lowercase)

a = [-1]*26

for idx,i in enumerate(letter):
  try:
    a[idx] = n.index(i)
  except:
    pass

for i in a:
  print(i, end=' ')
  
