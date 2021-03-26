# 1. 리스트 내 중복값 구하기 for loof 
# 2. 중복값의 인덱스값 구하기 
# 3. i < j 만족하는 배열 만들기
# 4. 3의 갯수 구하기 

nums = [1,2,3,1,1,3]
class Solution:
    def numIdenticalPairs(self, nums) :
        f={}
        ans=0
        for num in nums:
          if not num in f:
             f[num]=0
          f[num]+=1
        
        for num in f :
            n=f[num]
            ans+=(n*(n-1)//2)
        return ans