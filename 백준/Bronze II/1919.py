
# 문자열 두개 비교하여 같은 문자가 있으면 카운트 
# 문자열 두 개 길이 구해서 같은 문자x2 해서 빼줌

# 실패! 
string_1 = input()
string_2 = input()

cnt = 0

for i in string_1 :
  if i in string_2 :
    cnt +=1 

print(len(string_1)+len(string_2)-cnt*2)


## 검색 
Counter 

from collections import Counter 

s1 = Counter(input())   # Counter({'d': 2, 'a': 1, 'r': 1, 'e': 1})
s2 = Counter(input())   # Counter({'b': 1, 'r': 1, 'e': 1, 'a': 1, 'd': 1})

# 두 딕셔너리의 차집합 values를 더한 값을 출력한다
print(sum((s1-s2).values())+sum((s2-s1).values()))
# Counter({'d': 1}) + Counter({'b': 1})
