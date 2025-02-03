class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        maxi=1
        ic,dc=1,1
        inc=[1]*len(nums)
        dec=[1]*len(nums)
        for i in range(1,len(nums)):
            if nums[i]<nums[i-1]:
                ic+=1
                dc=1
            elif nums[i]>nums[i-1]:
                dc+=1
                ic=1
            else:
                ic=dc=1
            inc[i]=ic
            dec[i]=dc
        return max(max(inc),max(dec))
        