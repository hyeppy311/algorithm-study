## 코드 검색 

while True:
    try:
        lower_case, upper_case, number, blank = 0, 0, 0, 0
 
        for i in input():
            if i.islower():
                lower_case += 1
            elif i.isupper():
                upper_case += 1
            elif i.isdigit():
                number += 1
            else:
                blank += 1
        print(lower_case, upper_case, number, blank)
 
    except EOFError:      ## 입력이 끝날 때까지 값을 받고 끝나면 break
        break
      
      
## 입력값의 갯수가 지정되있지 않기 때문에 while문 으로 입력 받기.
## 소문자, 대문자, 숫자, 공백 변수지정 

## Boolean type
## islower(): 영어소문자
## isupper(): 영어대문자
## isdigit(): 숫자 
      
## EOFError : End Of File 파일의 끝. 

