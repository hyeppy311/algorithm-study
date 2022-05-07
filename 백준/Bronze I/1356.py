
# str으로 받아서 int로 바꿔줘야함 
# 각 자리수를 어떻게 변수에 저장할 것인가?

# 시도 
temp = []
mult = []
k = 1
q = n
for _ in range(len(q)-1) :
  temp.append(q.popleft())

# 리스트에 나눈 숫자들을 어떻게 한번에 선택해야 될지 계속 안풀림 ㅠㅠ

# 검색 
N = input()
ok = 0
for i in range(1, len(N)):
    s1, s2 = N[:i], N[i:]    # 슬라이싱으로 차례대로 하나씩 나눠줌 
    m1 = m2 = 1              # 곱해줄 변수
    for n in s1:
        m1 *= int(n)        # 나눠준 자리수를 for문으로 돌면서
    for n in s2:            # 곱해줌
        m2 *= int(n)
    if m1 == m2:            # 같으면 ok에 1 넣어주고
        ok = 1            
        break               # 멈춤
print("YES" if ok else "NO")      # 같은 수가 있으면 yes, 아니면 No 출려


# 복잡하게 생각하지말고 간단하게 생각하자
# 선택된 데이터를 어디에 넣을지 항상 변수 생각하기!!
