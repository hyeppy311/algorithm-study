

ls = [int(input()) for _ in range(5)]
ls.sort()

print(sum(ls)//len(ls))
print(ls[2])

## 중앙값은 개수가 홀수일 때 가운데수, 짝수일 때는 가운데 두 수의 평균값
