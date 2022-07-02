
a,b,c = map(int, input().split())


if a == b == c :
  print(10000 + a*1000)
elif a==b or a==c :
  print(1000 + a*100)
elif b == c :
  print(1000 + b*100)
else : 
  print(max(a,b,c) * 100)
  
  

 # 다른 풀이

lst = list(map(int, input().split()))
lst.sort()    # 숫자 정렬

s_lst = set(lst)  # 같은 숫자끼리 묶어줌 

# 모두 같은 수 일 경우
if len(s_lst) == 1 :    
  print(10000 + lst[0]*1000)
# 모두 다른 수 일 경우
elif len(s_lst) == 3 : 
  print(lst[2] * 100)
# 같은 눈이 2개일 경우 
else :
  print(1000 + lst[1]*100)
