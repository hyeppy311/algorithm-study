T = int(input())

for t in range(T) :
  pattern = input()
  
  for i in range(1,10+1) :               # 최대 마디의 길이가 10 
    if pattern[:i] == pattern[i:2*i] :   # 글자를 한 개씩 늘려가면서 비교해줌, 단어가 같으면 출력
      print(f'#{t+1} {i}')
      break
 

# 7번라인 출력
K O
KO RE
KOR EAK
KORE AKOR
KOREA KOREA
KOREAK OREAKO
KOREAKO REAKORE
KOREAKOR EAKOREAK
KOREAKORE AKOREAKOR
