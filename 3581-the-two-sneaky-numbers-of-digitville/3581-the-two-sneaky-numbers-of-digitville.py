class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
            return [i for i, n in Counter(nums).items() if n==2]
        