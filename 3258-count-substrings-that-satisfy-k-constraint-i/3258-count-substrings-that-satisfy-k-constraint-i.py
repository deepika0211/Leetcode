class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        n=len(s)
        total = n*(n+1)//2
        left = 0
        ones=0
        zeros=0
        invalid=0
        for r in range(n):
            if s[r]=='0':
                zeros+=1
            else:
                ones+=1
            while zeros>k and ones>k:
                invalid+=(n-r)
                if s[left]=='0':
                    zeros-=1
                else:
                    ones-=1

                left+=1
        return total-invalid

        