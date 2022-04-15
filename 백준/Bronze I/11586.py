

n = int(input())

mirror = [input() for _ in range(n)]

k = int(input())

tmp = []
if k == 1 :                       # k가 1일 경우는
  print(*mirror, sep='\n')        # 그대로 출력
elif k == 2 :                       # 2일 경우는 좌우반전
  for i in range(len(mirror)) :     
    tmp.append(mirror[i][::-1])     # 빈 리스트에 반대로 넣어서
  print(*tmp, sep='\n')             # 출력 
else :
  print(*mirror[::-1], sep='\n')    # 3일경우는 상하 반전. 거꾸로 출력
  
  
  
