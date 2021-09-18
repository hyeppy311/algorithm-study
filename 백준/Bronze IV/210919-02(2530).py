
h, m, s = map(int,input().split())
seconds = int(input())

hour = h*3600
minutes = m*60
sec = s


print(((hour+minutes+sec+seconds)//3600)%24,(hour+minutes+sec+seconds)%3600//60, 
(hour+minutes+sec+seconds)%3600%60%60)



## 변수명 짧게쓸순없을까..? 
