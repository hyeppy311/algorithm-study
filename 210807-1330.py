a,b = map(int, input().split())

def compare(A,B):
    
    if A > B :
        print('>')  #return '>' 
    if A < B :
        print('<')
    if A == B :
        print('==')

compare(a,b)
