class Solution(object):
    def plusOne(self, digits):
        c = 1
        for i in range(len(digits)-1,-1,-1):
            s = digits[i]+c
            digits[i]=s%10
            c=s//10
        if c:
            digits = [1]+digits
        return digits
        