

word = input()

cnt = 0 
vowel = 'aeiou'

for i in word : 
  if i in vowel :
    cnt += 1

print(cnt)
