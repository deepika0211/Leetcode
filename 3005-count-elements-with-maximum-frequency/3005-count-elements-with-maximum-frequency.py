class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq={}
        for i in nums:
            freq[i] = freq.get(i,0)+1
        a=max(freq.values())
        t=0
        for num in freq.values():
            if num==a:
                t+=num
        return t

        