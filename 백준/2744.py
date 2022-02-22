
## 내가 하고싶었던것

# 입력값을 for문에서 if문으로 isupper로 확인 후 대,소문자 변환

string = input()

lst = []
for i in string :
  if i.isupper():
    lst.append(i.lower())   ## 오타 확인좀.. 
  else :
    lst.append(i.upper())
    
print(*lst,sep='')



# 검색1

s= list(input())

for i in range(len(S)) :
  if s[i].islower() == True :   ## islower은 bool의 형태로 나오므로 True인지 확인을 해야함
    s[i]=s[i].upper()
  else :
    s[i]=s[i].lower()

print(''.join(s))

# 검색 2
s = input()
res = ''
for c in s : 
    if c.islower() :
        res += c.upper()
    else :
        res += c.lower()
print(res)

# 검색 3

a = input()
print(a.swapcase())  ## swapcase() 대문자는 소문자로, 소문자는 대문자로 바꿔주는 함수
