
# 문제
# 문자열로 들어오는 입력값 중 영어로 쓰여진 숫자를 숫자로 변경
# 입력 출력 예
# "one4seveneight"	1478


# 시도해본 코드

n = input()
nums = ["zero", "one", "two", "three", "four",
        "five", "six","seven","eight","nine"]

for i in nums :
  if i in n :
    n.replace(i.str(nums.index(i)))  # i는 변수일 뿐 n에 있는 영어로된 숫자를 지정해줘야함 # 계속 이부분에서 에러가 났음.ㅠㅠ

print(n)


# 검색

number = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def solution(s):
    answer = ''        # 답 입력
    word = ''          # 단어 입력 
    for i in s:
        if i.isdigit():        # 숫자인지 판단한 후 
            answer += i        # answer에 넣어주고
            continue           
        else:
            word += i          # 아닐경우 word에 넣어주고

            if word in number:   # 단어가 number에 있을 경우 
                answer += str(number.index(word))   # 인덱스값을 ans에 넣어주고 
                word = ''                           # word를 빈 리스트로 만들어줌

    answer = int(answer)        # str -> int로 변경

    return answer    

# dict 이용한 답
number = {"zero":0, "one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}

def solution(s) :
  ans = s
  for key,value in number.items():
    ans = ans.replace(key,str(value))  # replace는 인자로 str만 가능, 문자열에서만 사용.
    
  return int(ans)
  

# 처음에 isdigit를 사용하여 int는 판별했으나 문자를 어떻게 따로 담아줘야될지 몰랐음
# for문 사용시 문자를 하나씩 읽기 때문에 단어를 통째로 숫자로 변경할 수는 없음 -> 단어를 담아줄 변수를 따로 지정해야함 
# 어떤 것을 변경하는 문제는 제발 replace를 생각해라 

# 자꾸 실수하는 부분 
# 원소를 선택할 때는 담아줄 변수를 반드시 선언해줘야함!!! 

  
