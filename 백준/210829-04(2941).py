n = input()

cnt = len(n)

for i in range(cnt-1) :
  
  if (n[i] + n[i+1]) in ['c=','c-','d-','lj','nj','s=','z='] :
    cnt -= 1 
    if (n[i] + n[i+1]) == 'z=' and i > 0 and n[i-1] == 'd' :
      cnt -= 1

print(cnt)

