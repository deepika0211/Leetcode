class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        arr=[]
        c=0
        for row in grid:
            for i in row:
                arr.append(i)
        c=0
        for j in arr:
            if j<0:
                c+=1
        return c



        
