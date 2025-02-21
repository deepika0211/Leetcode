class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        res,sol=[],[]
        def venaka(i):
            if i==n:
                res.append(sol[:])
                return
            venaka(i+1)
            sol.append(nums[i])
            venaka(i+1)
            sol.pop()
        venaka(0)
        return res
        