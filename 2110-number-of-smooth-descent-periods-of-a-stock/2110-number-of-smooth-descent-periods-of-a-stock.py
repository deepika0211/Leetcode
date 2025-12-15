class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        ans=1
        leng=1
        for i in range(1,len(prices)):
            if prices[i]==prices[i-1]-1:
                leng+=1
            else:
                leng=1
            ans+=leng
        return ans