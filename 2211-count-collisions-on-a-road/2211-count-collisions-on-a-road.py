class Solution:
    def countCollisions(self, directions: str) -> int:
        l=0
        r=len(directions)-1
        while l<=r and directions[l]=="L":
            l+=1
        while l<=r and directions[r]=="R":
            r-=1
        c=0
        for i in range(l,r+1):
            if directions[i]!="S":
                c+=1
        return c
        

