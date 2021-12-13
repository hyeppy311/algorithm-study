


n = int(input())

result= 0

for i in range(1, n+1) :         ## 1부터 n까지
  A = list(map(int, str(i)))     ## 숫자를 담아서 분해! [1][2][3][4][5]....[2,1,6]  str으로 바꿔서 분해한 후 다시 숫자로 바꿔줌
  result = i + sum(A)            ## 생성자와 각 자리수 숫자의 합 -> N
  if result == n :               ## 같으면 생성자 출력하고 탈출
    print(i)
    break

  if i == n :                    ## 생성자가 없을경우 0 출력 
    print(0)
