## 정렬후 맨 앞의 값(최소) 제거

a,b,c,d,e,f = [int(input()) for _ in range(6)]

sub_1 = [a,b,c,d]
sub_2 = [e,f]
sub_1.sort()
sub_2.sort()
sub_1.pop(0)
sub_2.pop(0)

print(sum(sub_1)+sum(sub_2))



## 다 더한 후 최소값 제거

a,b,c,d,e,f = [int(input()) for _ in range(6)]

sub_1 = [a,b,c,d]
sub_2 = [e,f]

print(sum(sub_1)+sum(sub_2)-min(sub_1)-min(sub_2))


