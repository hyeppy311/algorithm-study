
# 처음 숫자입력을 제외하고는 같은 식이 반복됨 
# 변수를 어떻게 설정할지가 헷갈림.. 




## 검색 

input_num = int(input())    # 입력

num = input_num  # num 변수에 처음 입력값을 지정 
cnt = 0 # 반복문 카운트 

while True:
    sum_num = (num // 10) + (num % 10) # 각 자릿수를 더한 후 
    new_num = ((num % 10) * 10) + (sum_num % 10)  # 새롭게 만들어 지는 수를 변수에 저장 
    cnt += 1  # 사이클 카운트
    if new_num == input_num :    # 새롭게 만들어지는 수가 처음 입력값이랑 같으면 멈춤 
        break
    num = new_num  # 새롭게 만들어지는 수를 num에 저장하여 if문에서 걸릴때까지 반복 
    
print(cnt)



# 변수설정 시 새롭게 만들어지는 수의 변수를 설정해줬어야함 
# 문제에서 주어진 것을 보고 코드로 만드는 연습을 해야함 
