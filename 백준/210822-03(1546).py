
n = int(input())
a = list(map(int,input().split()))

b = [i/max(a)*100 for i in a]

print(sum(b)/len(b))


