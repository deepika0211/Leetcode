class Solution:
    def maxScore(self, s: str) -> int:
        res = 0
        zero = 0
        for i in range(len(s)-1):
            if s[i]=='0':
                zero+=1
            one = 0
            for j in range(i+1,len(s)):
                if s[j]=='1':
                    one+=1
            res = max(res,one+zero)
        return res