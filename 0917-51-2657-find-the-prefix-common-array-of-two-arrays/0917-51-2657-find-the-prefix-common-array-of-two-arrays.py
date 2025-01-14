class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n=len(A)
        s=[]
        c=[]
        count=0
        for i in range(n):
            a=A[i]
            b=B[i]
            if a==b:
                count+=1
            else:
                if a in s:
                    count+=1
                else:
                    s.append(a)
                if b in s:
                    count+=1
                else:
                    s.append(b)
            c.append(count)
        return c
        