# 8x8 체스판에서 나이트의 이동 가능 경우의 수 구하기

# 나이트는 수평으로 두 칸 이동 후 수직으로 한 칸 
# 수직으로 두칸 이동 후 수평으로 한 칸 이동 가능

# 열은 a~h, 행은 1~8로 되어있음 

# 입력 :  a1


# 코드리뷰 

input_data = input()
row = int(input_data[1])                   # 97
col = int(ord(input_data[0])) - int(ord("a")) + 1   # 아스키 코드를 사용하여 컬럼의 문자열을 숫자로 변환

steps = [(-2,-1), (-1,-2), (1,-2), (2,-1), (2,1), (1,2), (-1,2), (-2,1)]  # 나이트의 이동 가능한 방향

result = 0

for step in steps :
  next_row = row + step[0]     # 입력으로 받은 위치에 움직일 수 있는 이동거리를 더해줌 
  next_col = col + step[1] 
  
  # if 1 <= next_row <=8 and 1 <= next_col <= 8 :
  if next_row >= 1 and next_row <= 8 and next_col >= 1 and next_col <= 8 :   # 위치 값이 1~8에 있으면 이동가능 1 올려주고 
    result += 1

print(result) 


# 이동 후 위치나 이동 가능 경우의 수를 구할 때
# 입력으로 들어온 현재 위치를 변수에 저장
# 이동 가능 한 방향을 (x,y)의 형태로 리스트에 저장
# 현재 들어온 위치에 방향 리스트를 한번씩 돌면서 더해줌 
# 범위를 벗어나지 않는 조건을 꼭!! 지정해주고 
# 출력 
