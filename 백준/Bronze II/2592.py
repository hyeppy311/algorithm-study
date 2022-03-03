
numbers = list(int(input()) for _ in range(10))

print(sum(numbers)//len(numbers))    # 평균 

dic = {}
for i in numbers :
  if i in dic :
    dic[i] += 1
  else :
    dic[i] = 1
    
for k,v in dic.items() :
  if v == max(dic.values()) :
    print(k)                        # 최빈값
