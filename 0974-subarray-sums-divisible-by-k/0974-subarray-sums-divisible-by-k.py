class Solution(object):
    def subarraysDivByK(self, nums, k):
        count = 0
        prefix = 0
        r = {0: 1}
        for num in nums:
            prefix += num
            re = prefix % k
            if re < 0:
                re += k
            if re in r:
                count += r[re]
                r[re] += 1
            else:
                r[re] = 1
        return count
        
        