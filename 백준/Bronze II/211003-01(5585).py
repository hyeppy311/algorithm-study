## 코테책 참고해서 풀었음


cash = int(input()) 

change = 1000 - cash 

coin = [500,100,50,10,5,1]
cnt = 0

for i in coin : 
  cnt += change // i
  change %= i             ## i로 나눈 값이 change 변수에 저장되어 10라인에서 count 실행
  
print(cnt)
