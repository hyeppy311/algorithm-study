
# 1부터 n까지 들어있는 리스트 만들기 
# pop로 뽑아내고 append로 추가하기 


# 성공!! 
n = int(input())

cards = [i for i in range(1,n+1)]

tmp =[]
cnt = 0

while True:
  if cnt == n-1 :
    tmp.append(cards[0])
    break
  
  tmp.append(cards[0])      # 한줄로 나타내기 tmp.append(cards.pop(0)) 버리기
  cards.pop(0)                            
  cards.append(cards[0])    # cards.append(cards.pop(0)) 옮기기
  cards.pop(0)
  cnt +=1 

print(*tmp)



# 다른코드 검색

from collections import deque        # deque 공부해야할듭..? 

N = int(input())
queue = deque([i for i in range(1, N+1)])
while len(queue) > 1:
    print(queue.popleft(), end=' ')
    queue.append(queue.popleft())
print(*queue)

