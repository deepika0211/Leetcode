class Solution(object):
    def frequencySort(self, s):
        freq={}
        for ch in s:
            freq[ch]=freq.get(ch,0)+1
        highf = max(freq.values())
        bucket = [[]for i in range(highf+1)]
        for ch in freq:
            bucket[freq[ch]].append(ch)
        res=""
        for a in range(highf,0,-1):
            for ch in bucket[a]:
                res+=ch*a
        return res
        
        