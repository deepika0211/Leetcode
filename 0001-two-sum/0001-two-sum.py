class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_list={}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in nums_list:
                return [nums_list[diff],i]
            nums_list[num] = i