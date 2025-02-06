class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        prod={}
        c=0
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                p=nums[i]*nums[j]
                if p in prod:
                    prod[p]+=1
                else:
                    prod[p]=1
        for v in prod.values():
            if v>1:
                c+=(v*(v-1))//2*8
        return c
        