# 단어뒤집기 
# 단어를 리스트에 넣고 각각의 단어를 다시 리스트에 넣는다 [[happy],[today]]
# 리스트를 for문으로 돌려서 안에 있는 리스트에 reverse 적용

# 슬라이싱 활용하여 시도

# 출력형식 오류 
import sys
input = sys.stdin.readline

for _ in range(int(input())) :
  arr = list(map(str, input().split(" ")))
  
  ans = []
  for i in range(len(arr)) :
    ans.append(arr[i][::-1])
  print(*ans)    
  
  
# 검색 
  
import sys
 
n = int(sys.stdin.readline())
 
for _ in range(n):
  words = sys.stdin.readline().rstrip().split()   # readline은 개행문자를 포함, rstrip()으로 제거 후 split
 
  for word in words:
    print(word[::-1], end=' ')   # 역순으로 배열한 단어를 줄 바꿈 없이 출력 (문장 출력)

# 슬라이싱을 사용할 경우 굳이 리스트에 포함시키지 않아도 됨 
# 입력이 최대 1000이므로 readline 사용, readline 사용시 개행문자(\n) 꼭 제거해줘야 함 
