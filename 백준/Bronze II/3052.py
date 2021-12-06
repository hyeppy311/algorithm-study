

temp = []
for _ in range(10) :
  n = int(input())

  temp.append(n%42)

print(len(set(temp)))

## set() 중복원소 제거 후 리스트 생성
