class Solution(object):
    def canBeValid(self, s, locked):
        if len(s)%2!=0:
            return False
        openn=close=0
        for i in range(len(s)):
            openn += 1 if locked[i] == '0' or s[i]=='(' else -1
            if openn<0:
                return False
        for i in range(len(s)-1,-1,-1):
            close += 1 if locked[i] == '0' or s[i]==')' else-1
            if close<0:
                return False
        return True
        
        