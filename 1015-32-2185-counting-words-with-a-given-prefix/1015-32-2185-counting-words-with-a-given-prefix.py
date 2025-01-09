class Solution(object):
    def prefixCount(self, words, pref):
        r=0
        for i in words:
            if pref in i and i.index(pref)==0:
                r+=1
        return r
        