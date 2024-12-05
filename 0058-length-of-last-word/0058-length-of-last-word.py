class Solution(object):
    def lengthOfLastWord(self, s):
        l = s.strip()
        w = l.split(" ")
        return len(w[-1])
        