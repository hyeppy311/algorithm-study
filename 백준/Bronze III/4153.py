

while True :
  tri = list(map(int, input().split()))     ## 입력값이 여러줄일 때 while문으로 받아주고

  if sum(tri) == 0:                         ## 테스트 케이스 마지막 0,0,0 이면 탈출 
    break
  tri.sort()                                ## 세 수를 크기순으로 정렬

  if tri[0]**2 + tri[1]**2 == tri[2]**2 :   ## 피타고라스의 정리
    print('right')
  else :
    print('wrong')
