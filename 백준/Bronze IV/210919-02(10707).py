

a = int(input())          ## X사 1리터당 요금
b = int(input())          ## Y사 기본요금
c = int(input())          ## Y사 사용량 상한 
d = int(input())          ## Y사 1리터당 추가요금
p = int(input())          ## J군 한 달간 수도양 p 리터

if p < c :
  print(min(a*p,b))

elif p > c :
  print(min(a*p, b+(p-c)*d))
