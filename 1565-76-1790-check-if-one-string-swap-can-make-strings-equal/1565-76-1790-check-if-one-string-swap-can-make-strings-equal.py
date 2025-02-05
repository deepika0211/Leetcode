class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1==s2:
            return True
        elif Counter(s1)!=Counter(s2):
            return False
        c=0
        a=[]
        for i,j in enumerate(s1):
            if j!=s2[i]:
                c+=1
                a.append(i)
        if c==2:
            if s1[a[0]]==s2[a[1]] and s1[a[1]]==s2[a[0]]:
                return True
        return False
        