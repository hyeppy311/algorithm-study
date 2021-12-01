

a,b,c = (int(input()) for _ in range(3))

multi = list(str(a*b*c))

z = 0
one = 0 
two = 0
three = 0
four = 0
five = 0
six = 0
seven = 0 
eight =0 
nine = 0

for i in multi :
  if i == "0" :
    z+=1 
  if i == "1" :
    one+=1 
  if i == "2" :
    two+=1
  if i == "3" :
    three+=1
  if i == "4" :
    four+=1
  if i == "5":
    five+=1
  if i == "6":
    six+=1
  if i == "7":
    seven+=1
  if i == "8":
    eight+=1
  if i == "9":
    nine+=1

print(z,
one,
two,
three,
four ,
five ,
six ,
seven , 
eight , 
nine , sep='\n')

## 처음제출에서는 srt.count()ㄹ
ㅡ
ㅡㄹ
