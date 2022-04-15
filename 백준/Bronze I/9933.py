
# 리스트 내 원소(str) 중 원래 문자열과 반대의 문자열을 포함 한 경우 문자열의 길이와 가운데 문자를 출력

n = int(input())

words = []
for _ in range(n) :
  words.append(input())

for word in words :
  if word[::-1] in words : 
    break
print(len(word),word[len(word)//2])


