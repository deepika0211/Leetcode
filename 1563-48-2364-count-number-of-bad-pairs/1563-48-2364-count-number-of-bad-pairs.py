class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        fre={}
        pair=0
        for i,num in enumerate(nums):
            k=num-i
            pair+=fre.get(k,0)
            fre[k]=fre.get(k,0)+1
        n=len(nums)
        return (n*(n-1))//2-pair
        