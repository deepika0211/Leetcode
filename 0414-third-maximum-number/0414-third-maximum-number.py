class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        a = list(set(nums))
        a.sort(reverse=True)
        if len(a)>=3:
            return a[2]
        else:
            return a[0]