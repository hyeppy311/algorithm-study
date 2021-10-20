

a,b,c,d = [list(map(int, input().split())) for i in range(4)]

remain_1 = a[1] - b[0] + b[1]
remain_2 = remain_1 - c[0] + c[1]
remain_3 = remain_1 - d[0]

print(max(remain_1, remain_2, remain_3))




