
T = int(input())

for t in range(1, T+1) :
    N = int(input())

    pascal = [ [1], [1,1] ]       # 위의 2줄 만들어줌
    for i in range(2, N) :        # 3번째 줄 부터 생성 
        list = [1]                # 1부터 시작하니까 미리 넣어주고
        for j in range(i-1) : 
            list += [pascal[i-1][j] + pascal[i-1][j+1]]  # 위 왼쪽,오른쪽 숫자 더해서 리스트에 추가
        list += [1]               # 마지막 숫자 1 리스트에 추가
        pascal += [list]          # 삼각형을 만들 리스트에 추가

    print("#{}".format(t))
    for i in range(N) :
        print(*pascal[i])
