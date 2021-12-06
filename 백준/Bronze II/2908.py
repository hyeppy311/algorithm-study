

a, b = input().split()

n = "".join(reversed(a))
m = "".join(reversed(b))

print(max(int(n),int(m)))


## reverse와 reversed는 string에선 안댐...! 
# 변환 후에 다른 조치를 해야됨 
