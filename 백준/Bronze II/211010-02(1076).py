## 문자:숫자

a,b,c = [input() for _ in range(3)]

colors = {"black":0,"brown":1,"red":2,"orange":3,"yellow":4,
          "green":5,"blue":6,"violet":7,"grey":8,"white":9}

a1 = colors[a]*10
b1 = colors[b]
c1 = 10**colors[c]

print(a1*c1 + b1*c1)


## 더 쉬운 방법, 문자:문자로 딕셔너리 만들기

a,b,c = [input() for _ in range(3)]

colors = {"black":'0',"brown":'1',"red":'2',"orange":'3',"yellow":'4',
          "green":'5',"blue":'6',"violet":'7',"grey":'8',"white":'9'}


print(colors[a]+colors[b]+'0'*int(colors[c]))
