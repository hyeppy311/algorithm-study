
# 키패드 배열을 2차원으로 선언
# 오른손, 왼손 지정된 키패드 숫자 정의 
# 입력으로 들어온 손의 시작점 설정 : 오른손 "#" , 왼손 "*"



# 시도
# 입력예시 
nums = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
used_hand = "right"


r = [3,6,9]
l = [1,4,7]

ans = ""
for i in nums :
  if i in r :
    ans += "R"
  else :
    ans += "L"

print(ans) 

# 오른손 왼손 까지는 구현했는데 2,5,8,0 가운데 숫자가 들어오는 경우를 구현해야함 
# 키패드를 좌표로 변경해서 현재 위치한 손가락에서 더 가까운 거리를 계산해줘야함 

# 검색 
# 입력 숫자가 2,5,8,0 일 경우 
def pos(num, left, right, hand):
    
    kp = {                                # 좌표를 딕셔너리로 선언
        1:(0,0), 2:(0,1), 3:(0,2),
        4:(1,0), 5:(1,1), 6:(1,2),
        7:(2,0), 8:(2,1), 9:(2,2),
        '*':(3,0), 0:(3,1), '#':(3,2)
    }

    # 좌표 거리 계산 (현재 2,5,8,0 중 하나의 위치(좌표)에서 현재 오른손 좌표, 왼손 좌표를 각각 빼준 후 더해줌) 
    dist_left = abs(kp[num][0] - kp[left][0]) + abs(kp[num][1] - kp[left][1])
    dist_right = abs(kp[num][0] - kp[right][0]) + abs(kp[num][1] - kp[right][1])

    # 더한 숫자(거리)가 더 작은 손가락을 리턴 
    if dist_left < dist_right:
        return 'L'
    elif dist_left > dist_right:
        return 'R'
    # 거리가 같은 경우 오른손잡이면 R, 왼손잡이면 L 출력
    else:
        if hand == 'right':
            return 'R'
        else:
            return 'L'


def solution(nums, hand):
    result = ''
    # 현재 위치 지정
    left = '*'
    right = '#'

    for num in nums:
        if num in [1, 4, 7]:	# 1,4,7 이면 왼손
            result += 'L'
            left = num        # 마지막 왼손 위치 저장
        elif num in [3, 6, 9]:	 # 3,6,9 이면 오른손
            result += 'R'        # 마지막 오른손 위치 저장
            right = num
        else:                   # 입력된 숫자가 2, 5, 8, 0일 경우
            mid = pos(num, left, right, hand)  # 위에 pos() 함수에 넣어줌
            result += mid                      # 결과로 나온 손을 result에 저장
            if mid == 'R':                     # pos() 함수에서 나온 값이 오른손이면
                right = num                    # 오른손에 현재 위치값 (2,5,8,0) 저장
            else:
                left = num                     # 왼손이면 왼손에 저장 
            
    return result


# 또 다른 코드 

def solution(numbers, hand):
    answer = ''
    key_list = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'], ['*', '0', '#']]   # 키패드를 2차원 리스트로 선언
    left = '*'           # 현재 엄지손가락의 위치 선언
    right = '#'          
    
    for num in numbers:          # 입력으로 들어온 숫자를 돌면서
        flag = ''         
        if num in [1, 4, 7]:      # 1,4,7 이면    
            flag = 'L'            # 왼손 저장
        elif num in [3, 6, 9]:    # 3,6,9 이면
            flag = 'R'            # 오른손 저장
        else:                     # 2,5,8,0 일 경우
            for i in range(len(key_list)):           # 키패드 리스트 길이만큼 돌면서 0,1,2,3 
                for j in range(len(key_list[i])):    # 키패드를 담은 리스트 길이만큼 돌기 0,1,2
                    if left == key_list[i][j]:      # left가 "*"일 경우
                        l_loc = [i, j]               # 왼손의 위치 [3,0]
                    if right == key_list[i][j]:     # right가 "#"일 경우
                        r_loc = [i, j]               # 오른손 위치 [2,3]
                    if str(num) == key_list[i][j]:  # 2,5,8,0 중 하나의 위치 저장 
                        n_loc = [i, j]
            
            l_len = abs(n_loc[0]-l_loc[0]) + abs(n_loc[1]-l_loc[1])    # 2,5,8,0 중 특정 위치에서 왼손,오른손 좌표 빼줌
            r_len = abs(n_loc[0]-r_loc[0]) + abs(n_loc[1]-r_loc[1])
             
            if l_len < r_len:    # 오른손과 왼손 위치 길이 비교후 작은 값의 손 저장 
                flag = 'L'        
            elif r_len < l_len:  
                flag = 'R' 
            else:                    # 같을 경우, 입력으로 들어온 값에 따라 손 저장
                if hand == 'left':
                    flag = 'L'
                else:
                    flag = 'R'
                    
        if flag == 'L':        # 출력값 저장후 현재위치 손가락 위치 갱신
            answer += 'L'      
            left = str(num)  
        else:
            answer += 'R'
            right = str(num)

    return answer
