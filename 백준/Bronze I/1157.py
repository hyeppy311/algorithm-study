
# 입력값을 리스트로 받고 
# 알파벳 갯수를 알파벳(key), 갯수(value)로 딕셔너리에 저장 
# value가 제일 큰 값의 알파벳을 출력 


# 틀림 
word = list(input())

tmp = dict()

for i in word : 
  if tmp.get(i) :
    tmp[i] += 1
  else: 
    tmp[i] = 1

# if len(max(tmp,key=tmp.get)) == 1:   # 최대값이 한개일때 
#   print(max(tmp,key=tmp.get))
# else :
#   print("?")
  
ans = []
for k,v in tmp.items() :
  if v == max(tmp.values()) :
    ans.append(k)
   
if len(ans) == 1 :   # 대소문자 변경하는 과정에서 아스키 코드 사용했는데 할 필요 없음
  s = ord(k) - 32
  print(chr(s))
else :
  print("?")

# 알파벳이 같을 경우 대소문자를 각각의 key로 인식해서 오류남  -> # 알파벳을 모두 소문자로 변경하거나 대문자로 변경해야함
# 입력할 때 upper() 함수 사용 

# 수정된 코드

word = list(input().upper())

tmp = dict()

for i in word : 
  if tmp.get(i) :
    tmp[i] += 1
  else: 
    tmp[i] = 1
  
ans = []
for k,v in tmp.items() :
  if v == max(tmp.values()) :
    ans.append(k)
    
if len(ans) > 1:
  print("?")
else :
  print(*ans)
  

# 간결한 코드 검색

word = input().upper()
word_list = list(set(word))     ## 중복되는 알파벳을 묶어줌

cnt = []
for i in word_list:        # 알파벳 하나씩을 
  count = word.count       # 갯수를 세어서
  cnt.append(count(i))     # 빈 리스트에 추가

if cnt.count(max(cnt)) > 1:  # 최대값이 1개 이상일경우 ? 출력 
  print("?")

else:
  print(word_list[(cnt.index(max(cnt)))])  # 최대값의 인덱스 출력
  
  
  

  
