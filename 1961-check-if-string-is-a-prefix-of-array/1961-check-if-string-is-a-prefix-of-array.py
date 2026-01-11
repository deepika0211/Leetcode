class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        dupe=""
        for i in words:
            dupe+=i
            if dupe==s:
                return True
            if len(dupe)>len(s):
                return False
        return False
        