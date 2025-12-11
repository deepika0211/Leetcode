class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len=float('inf')
        totl=0
        l=0
        for r in range(len(nums)):
            totl+=nums[r]
            while totl>=target:
                min_len=min(min_len,r-l+1)
                totl-=nums[l]
                l+=1
        return min_len if min_len<float('inf') else 0
        
        