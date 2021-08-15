n = list(map(int,input()))

a = n[0]
b = n[1]

cycle = 0


while True: 
  if a+b < 10 : 
    c = list(format(a+b, '02'))
    c_sum = c[0] + c[1]
  else : 
    a+b

  sums = int(a+b)
  sums1 = sums[0] + sums[1]
  
  cycle = cycle + 1 

  if (n == sums1):
    break
    print(cycle)
