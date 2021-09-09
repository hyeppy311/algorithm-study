n = int(input()) -1 

answer = 1
temp = 6
while n > 0 :
    n -= temp 
    answer += 1
    temp += 6
    
print(answer)
