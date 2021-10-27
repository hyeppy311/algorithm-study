
n , k = map(int,input().split())

tmp = []
for i in range(1,n+1) :
  if n % i == 0 :
    tmp.append(i)

print(tmp[k-1] if len(tmp)>=k else 0)
