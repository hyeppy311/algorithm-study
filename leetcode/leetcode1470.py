1470. Shuffle the Array

# 1. 리스트길이 구하기
# 2. 길이를 반으로 나눈 값 구하기 
# 3. 그 값을 시작으로 슬라이싱 
# 4. 나머지 리스트와 3에서 구한 리스트 합치기 (못함) 

nums = [2,5,1,3,4,7]

numslength = int(len(nums))  #리스트 길이
cut = int(numslength / 2)  #반으로 나눈 값

a = (nums[cut : ]) # 나눈 값 부터 슬라이싱 
b = (nums[ :cut ]) # 반띵된 리스트 (여기다 껴넣기)  

# n 빼먹어서 머리터짐 

# 답

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        answer = []      
        
        for i in range(len(nums) // 2) :   
            answer.append(nums[i])    
            answer.append(nums[i+n])

        return answer
      
      
      
