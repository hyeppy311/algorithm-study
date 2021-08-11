# 내가 시도한것..  -> 자꾸 컴파일에러남..unexpected indent (Main.py3, line 3)

while True :
  a,b = map(int, input().split())
    print(a+b)


# 답
while True:
    try:
        A, B = map(int, input().split())
        print(A+B)
    except:
        break

# 문제에서 입력 갯수가 정해지지 않았기때문에..try, except 해줘야함 
# 엉뚱한 값 들어가면 except로 가서 종료
