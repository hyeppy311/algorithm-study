
## 성공!! 

T = int(input())

for _ in range(T) :
  N = int(input())
  
  dic = {}                       # 입력값이 대학이름 소비량 나눠져 있어 딕셔너리로 저장
  for _ in range(N) :
    uni,bottles = input().split()     # 입력에서 학교이름이랑 소비량으로 나누고
    dic[uni]=int(bottles)             # 선언해준 딕셔너리 key에 value 입력 (입력 시 str을 int로 바꿔줌) 
  
  for k,v in dic.items() :            # k-key, v-value로 변수 나눠 주고
    if v == max(dic.values()) :       # value중 최대값이 v면 
      print(k)                        # key 값 출력
      

      
# 다른 코드 검색 

T = int(input()) 
for _ in range(T): 
  N = int(input()) 
  max = 0 
  mName = "" 
  for _ in range(N): 
    name, num = input().split()      # 나눠주고
    num = int(num)                   # int로 바꾼뒤
    if(num > max):                   # 선언해준 max와 비교하여 
      max = num                      # num 더 크면 저장
      mName = name                   # 그때 이름 저장
  print(mName)                       # 출력 
 
# 딕셔너리를 사용하지 않고 max 최대값을 저장하고 계속 비교하는 방식. 



