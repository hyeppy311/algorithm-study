a,b = map(int, input().split())

# 1.input()으로 입력받은 값은 문자열임
# 2.split()공백으로 값 분리
# 3.int 정수로변경
# 4.map(함수,반복가능한 자료형) 반복객체로 받은 값들을 함수로 변경해줌, python3에선 리스트나 튜플 형태로 지정해줘야함.


def compare(A,B):
    
    if A > B :
        print('>')  #return '>' 
    if A < B :
        print('<')
    if A == B :
        print('==')

compare(a,b)
