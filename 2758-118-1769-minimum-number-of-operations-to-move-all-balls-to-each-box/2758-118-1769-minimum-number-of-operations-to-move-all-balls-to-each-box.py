class Solution(object):
    def minOperations(self, boxes):
        n=len(boxes)
        a=[0]*n
        for i in range(n):
            r=0
            for j in range(n):
                if boxes[j]!='0' and i!=j:
                    r+=abs(i-j)
                a[i]=r
        return a
        