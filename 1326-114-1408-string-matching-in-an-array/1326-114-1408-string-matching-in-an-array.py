class Solution(object):
    def stringMatching(self, words):
        r=[]
        n=len(words)
        for i in range(n):
            for j in range(n):
                if i!=j and words[i] in words[j]:
                    r.append(words[i])
                    break
        return r
        