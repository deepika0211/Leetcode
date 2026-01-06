class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = s.strip()
        w = l.split(" ")
        return len(w[-1])