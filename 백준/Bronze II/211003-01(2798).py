

## n개의 카드중에서 3장을 뽑아 m에 근접한 숫자의 합

n,m = map(int,input().split())
card = list(map(int,input().split()))

sums = []
for i in range(n-2) :           ##                                                                
    for j in range(i+1,n-1) :
        for k in range(j+1,n) :
            if card[i]+card[j]+card[k] <= m :
                sums.append(card[i]+card[j]+card[k])

print(max(sums))

