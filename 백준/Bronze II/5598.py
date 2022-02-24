

n = input()
ans = []

for i in n :
  if i in 'ABC' :
    ans.append(chr(ord(i)+23))   ## 암호알파벳에서 숫자를 빼야 원래 알파벳이 되지만 ABC는 23을 더해줘야 XYZ가 된다. 
  else :
    ans.append(chr(ord(i)-3))

print("".join(ans))
