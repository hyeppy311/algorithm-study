# 내가 푼 답

n,x = map(int,input().split())
a = list(range(1,1+n))   # n값을 받아와서 리스트를 만드는것임.. 


for i in a : 
  if i < x :
    print(i, end = ' ')
    

# 문제에서 요구하는 입력값
10 5
1 10 4 9 2 3 8 5 7 6 -> 이거 넣어줄 리스트 만들어야함..
-> 이것으로 수정 a = list(map(int, input(),split())
