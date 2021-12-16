

t = int(input())

for _ in range(t) :
  n = int(input())

  room = ['o'] * n
  for i in room : 
    for j in range(2,n-1) :
      for k in range(1,n-1) :
        if i == 'o' :
          room[j*k] = 'x'
        # else :
        #   room[j*k] = 'o'

  print(room.count('o'))
  
  돌아버리겐네.. 
