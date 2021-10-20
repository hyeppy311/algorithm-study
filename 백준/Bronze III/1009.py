## 1차 제출 

import sys 
input = sys.stdin.readline

t = int(input())

for _ in range(t) :
  a,b = map(int, input().split())

  for i in range(1,11) :
    if a ** b % 10 == i :
      print(i)
      
## 시간초과... 



## 검색 코드 .. 

import sys
data_cnt = int(sys.stdin.readline())
for _ in range(data_cnt):
    a, b = map(int, sys.stdin.readline().split())
    result = [(a ** i) % 10 for i in range(1,5)][(b % 4) -1]
    print(result if result != 0 else 10)    ## reuslt가 0이 아니라면 result 출력, 맞다면 10 출력

## 컴퓨터가 10대 데이터의 갯수는 a^b의 갯수로 주어짐, 10으로 나누어 나온 나머지가 컴퓨터의 숫자
## 1~9 까지 각 숫자의 거듭제곱 수의 일의 자리 수 규칙이 있음 
## 4개마다 순환이 됨 ex) 2의 거듭제곱은 2,4,8,6,2,4,8,6...의 순서로 감 
## 라인25 입력받은 수(a)를 1부터 4까지 거듭제곱해서 10으로 나눈 값을 리스트로 만들고 
## 제곱횟수인 b를 4로 나눠서 나온 나머지의 인덱스 값이 답! (인덱스는 0부터 시작하니깐 -1) 
## 일의자리 숫자가 0이면 (10,20,30..) 10번째 컴퓨터 
