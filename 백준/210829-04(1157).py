
n = input().upper()

st = set(list(n))

dic = dict()
for i in list(st):
  dic[i] = 0

for i in n:
  dic[i] += 1

lst = list(dic.items())
lst.sort(key = lambda x : (-x[1],x[0]))

if len(lst)==1 or lst[0][1] != lst[1][1]:
  print(lst[0][0])
else:
  print('?')

