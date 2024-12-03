class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        ans = 0
        for i in range(len(operations)):
            temp = operations[i]
            if temp == "--X" or temp == "X--":
                ans-=1
            else:
                ans+=1
        return ans