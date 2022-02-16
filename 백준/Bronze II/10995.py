

N = int(input())

if N == 1 :
  print("*")

else :
    for i in range(N) :
        if i % 2 == 0 :      # 처음에 N을 i로 해서 답이 안나왔음
          print("* " * N)    # 입력값과 별의 갯수가 같아야함 
        else :
          print(" *" * N)
