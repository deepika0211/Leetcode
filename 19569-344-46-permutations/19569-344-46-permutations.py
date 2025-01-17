class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        ans,sol=[],[]
        def venaka():
            if len(sol)==n:
                ans.append(sol[:])
                return
            for i in nums:
                if i not in sol:
                    sol.append(i)
                    venaka()
                    sol.pop()
        venaka()
        return ans
        