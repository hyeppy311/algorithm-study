n = int(input())

for i in range(5) :

  if (n-3*i)%5 == 0 :
    print(i+(n-3*i)//5)
    break 

  if (n-3*i)< 0 :
    print(-1)
    break
    
