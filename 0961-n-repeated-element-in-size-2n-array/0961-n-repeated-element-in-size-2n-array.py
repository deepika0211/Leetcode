
class Solution(object):
    def repeatedNTimes(self, nums):
        a=set()
        for i in nums:
            if i not in a:
                a.add(i)
            else:
                return i




        