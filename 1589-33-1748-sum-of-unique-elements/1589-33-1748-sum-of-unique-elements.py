class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        s=0
        nums=Counter(nums)
        for i,j in nums.items():
            if j==1:
                s+=i
        return s
        