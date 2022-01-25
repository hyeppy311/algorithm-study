

n = int(input())

tmp = dict()
for _ in range(n) :
  name = input()[0]         # 첫 글자만 받기
  if tmp.get(name):         # key가 딕셔너리에 있는경우 대응하는 value값을 돌려줌
    tmp[name] += 1          # key에 대응하는 value값을 하나씩 추가
  else: tmp[name] = 1       # value값을 1로 만들어 


lst = sorted([k for k,v in tmp.items() if v >= 5])  # k는 key, v는 value로 설정. v의 값이 5이상이 되는 k값을 리스트에 저장

print("".join(lst))



n = int(input())

tmp = dict()
for _ in range(n) :
  name = input()[0]
  if tmp.get(name) :
    tmp[name] += 1
  else : 
    tmp[name] = 1

answer = []
for k,v in tmp.items():
  if v >= 5 : 
    answer.append(k)

answer.sort()

if not answer : print("PREDAJA" )    
else : print(''.join(answer))
  
