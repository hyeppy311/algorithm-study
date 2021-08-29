## 가장많이 사용된 알파벳 세기 


n = input().upper()               ## 대소문 구분없음, 입력값 대문자로 변환 

st = set(list(n))                 ## 중복값 묶기 
 
dic = dict()
for i in list(st):                ## 인자 key 값으로 넣고 value 0을 만들기
  dic[i] = 0

for i in n:                       ## 인자 있으면 하나씩 더하기
  dic[i] += 1

lst = list(dic.items())                        ## items() : key, value를 튜플 형태로 리스트로 만들어 반환 [(key, value)]
lst.sort(key = lambda x : (-x[1],x[0]))        ## 알파벳이 많은 순서대로 정렬

if len(lst)==1 or lst[0][1] != lst[1][1]:      
  print(lst[0][0])                            ## value값이 제일 큰 인덱스 출력
else:
  print('?')

