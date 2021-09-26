a,b,c,d,e,f = [int(input()) for _ in range(6)]

sub_1 = [a,b,c,d]
sub_2 = [e,f]
sub_1.sort()
sub_2.sort()
sub_1.pop(0)
sub_2.pop(0)

print(sum(sub_1)+sum(sub_2))
