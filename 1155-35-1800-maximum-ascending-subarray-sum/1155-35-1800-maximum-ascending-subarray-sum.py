class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        maxm=0
        a=nums[0]
        n=len(nums)
        for i in range(1,n):
            if nums[i-1]>=nums[i]:
                maxm=max(a,maxm)
                a=nums[i]
            else:
                a+=nums[i]
        return max(a,maxm)
        