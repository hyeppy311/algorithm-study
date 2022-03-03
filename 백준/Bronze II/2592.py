
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

    
# 원소의 갯수를 세주는 라이브러리 

from collections import Counter

cnt = Counter(numbers)
print(cnt)

>>>
Counter({30: 3, 40: 2, 60: 2, 10: 1, 20: 1, 50: 1})


numbers = [int(input()) for i in range(10)]
print(sum(numbers)//10)
print(max(numbers, key = numbers.count))

