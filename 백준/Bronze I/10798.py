
# 입력시 첫번째 글자부터 하나씩 받을 순 없을까 ? 
# 다 입력받고 for문 돌려가며 리스트에 넣어야될까? 


# 공백이 없는 문자에서는 출력이 됐지만 공백이 있는 경우 str의 길이와 리스트의 인덱스 길이가 달라서 오류남(line13)

arr = list(input() for _ in range(5))

words = []
for i in range(len(arr)) :
  for j in range(len(arr)) :
    words.append(arr[j][i])
print("".join(words))


# 공백이 있는 문자열을 그대로 받을 수 있는 방법을 검색했지만 못찾음

# 문제 조건
# 세로로 읽은 순서대로 글자들을 출력한다. 이때, 글자들을 공백 없이 연속해서 출력한다. 
# while문으로 하는게 나을까? 


# 검색 
words = []
word_len = []

for _ in range(5) :
  word = input()
  words.append(word)             # 단어를 리스트에 담고,
  word_len.append(len(word))     # 단어의 길이도 리스트에 담아준다. 

ans = ''
for i in range(max(word_len)):   # 제일 긴 단어의 끝까지 담아야하기 때문에   [0][0], [1][0], [2][0], [3][0]...
  for j in range(5) :            # 리스트안에는 5개의 단어가 있으니깐 5번 돌려줌 
    if i < word_len[j] :         # 단어길이와 비교하여 i가 더 작으면 단어를 담아줌, 같을 경우 다시 34라인 for문으로 올라가서 반복
      ans += words[j][i]

print(ans)

# 검색2 조금 더 간결한 코드 

words = []
for _ in range(5) :
  word= input()
  words.append(word)
  
for i in range(max(len(k) for k in words)): 
  for j in range(5) :
    if i < len(word[j]) :
      print(words[j][i], end ='') 

 

# 첫번째 글자부터 차례대로 담는 방법은 생각했으나 글자가 짧은 경우를 해결하지 못했음
# 제일 긴 글자만큼 반복해주고 글자의 길이가 더 클때 출력해주는게 요점! 
# for문은 조건에 맞지 않으면 다시 처음부터 시작한다. 

