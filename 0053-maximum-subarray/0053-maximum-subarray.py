class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = final = nums[0]
        for num in nums[1:]:
            curr=max(num,curr+num)
            final = max(final,curr)
        return final


        