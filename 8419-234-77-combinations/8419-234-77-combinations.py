class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans, sol =[], []
        def comb(x):
            if len(sol)==k:
                ans.append(sol[:])
                return
            left=x
            need=k-len(sol)
            if left>need:
                comb(x-1)
            sol.append(x)
            comb(x-1)
            sol.pop()
        comb(n)
        return ans
        