class Solution:
    def clearDigits(self, s: str) -> str:
        a=[]
        for i in s:
            if ord('0')<=ord(i)<=ord('9'):
                a.pop()
            else:
                a.append(i)
        return "".join(a)
        