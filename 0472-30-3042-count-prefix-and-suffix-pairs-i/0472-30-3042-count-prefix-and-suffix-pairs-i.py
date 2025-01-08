class Solution(object):
    def countPrefixSuffixPairs(self, words):
        a=len(words)
        if a<2:
            return 0
        c=0
        for i in range(a):
            s1=words[i]
            for j in range(i+1,a):
                s2=words[j]
                if s2.startswith(s1) and s2.endswith(s1):
                    c+=1
        return c
        
        