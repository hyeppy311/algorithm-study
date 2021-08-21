l = [True for _ in range(10000)]
for a in range(10):
  for b in range(10):
    for c in range(10):
      for d in range(10):

        n = 2*a+11*b+101*c+1001*d
        if n < 10000 :
          l[n] = False

for i in range(10000):
  if l[i] :
    print(i)
