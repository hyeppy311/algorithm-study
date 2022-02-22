
a,b = input().split()

min = int(a.replace('6','5')) + int(b.replace('6','5'))
max = int(a.replace('5','6')) + int(b.replace('5','6')) 

print(min,max)



## if문 쓸 필요 없이 바로 변경하는게 간결함
