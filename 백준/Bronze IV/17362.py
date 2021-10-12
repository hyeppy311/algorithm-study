
# 1,9,17...마다 엄지손가락
# 8로 나눈 나머지를 설정 


n = int(input())
n = n%8
if n ==1 : print(1)
elif n in [2,0] : print(2)
elif n in [3,7] : print(3)
elif n in [4,6] : print(4)
elif n == 5 : print(5)

