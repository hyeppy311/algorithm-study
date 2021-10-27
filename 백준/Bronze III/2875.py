# 대회에 나갈 때 2명의 여학생과 1명의 남학생이 팀을 결성
# N명의 여학생과 M명의 남학생이 팀원, 학생들 중 K명은 반드시 인턴쉽 프로그램에 참여,인턴쉽 참여학생 팀 안됨
# 여학생의 수 N, 남학생의 수 M, 인턴쉽에 참여해야하는 인원 K가 주어질 때 만들 수 있는 최대의 팀 수


## 그리디로 해결

women,men,intern = map(int,input().split())

team = 0

while  women >=2 and men >=1 and women+men - 3 >= intern :   
  women -= 2
  men -= 1
  team += 1

print(team)
