
a=[int(input()) for _ in range(9)]   ## 입력값 9개 받아야되니까 range로 9번 input 

b = max(a)
print(b)
print(a.index(b)+1)

