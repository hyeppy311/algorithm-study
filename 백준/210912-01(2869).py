a,b,v=map(int,input().split())

spot=v-a
day=spot//(a-b)
if spot%(a-b):
  day+=2
else:
  day+=1

print(day)
