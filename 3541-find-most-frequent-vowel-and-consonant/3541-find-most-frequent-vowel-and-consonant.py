class Solution:
    def maxFreqSum(self, s: str) -> int:
        freq={}
        for ch in s:
            if ch in freq:
                freq[ch]+=1
            else:
                freq[ch]=1
        a="aeiouAEIOU"
        v=0
        c=0
        for ch, count in freq.items():
            if ch in a:
                v = max(v,count)
            else:
                c = max(c,count)
        return v+c
                


        