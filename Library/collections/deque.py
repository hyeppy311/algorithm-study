'''
stack과 queue를 합친 기능
iterable 데이터
일반 리스트와는 달리 양쪽에서 데이터를 추가,추출,삭제 할 수 있다. 
데이터의 길이는 속성 maxlen을 지정해 주지 않으면 임의로 커진다. 
'''

# 사용가능한 메소드
['append', 
 'appendleft', 왼쪽에 자료 추가 
 'clear', 
 'copy', 
 'count', 
 'extend', 
 'extendleft', 왼쪽에 리스트 확장 
 'index', 
 'insert', 
 'maxlen', 
 'pop', 
 'popleft', 왼쪽에서 원소 추출후 반환. 변수에 저장 가능 
 'remove', 
 'reverse', 
 'rotate'  rotate(n) 양수면 오른쪽으로 회전, 음수면 왼쪽으로 회전    
]

# 예시

from collections import deque 

d = deque(["happy","birth","day"]) # 객체 선언

d.append("to")
print(d)
# deque(['happy', 'birth', 'day', 'to'])

d.appendleft("you")
print(d)
# deque(['you', 'happy', 'birth', 'day', 'to'])

d.rotate(2)
print(d)
# deque(['day', 'to', 'you', 'happy', 'birth'])

temp = d.popleft()
print(temp)
day
print(d)
deque(['to', 'you', 'happy', 'birth'])

# BFS 탐색시 앞에서 데이터를 꺼내기 때문에 많이 사용됨 

