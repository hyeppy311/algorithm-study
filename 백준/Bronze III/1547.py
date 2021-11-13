

lst = [0,1,0,0]  ## 공의 위치를 나타내는 리스트
n = int(input())

for _ in range(n) :
  x,y = map(int, input().split())

  lst[x],lst[y] = lst[y],lst[x]   ## 공의 위치를 바꿔줌 

print(lst.index(1))  ## 공의 위치 출력

