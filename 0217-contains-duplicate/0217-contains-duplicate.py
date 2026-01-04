class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        notdup=set()
        for i in nums:
            if i in notdup:
                return True
            notdup.add(i)
        return False
        