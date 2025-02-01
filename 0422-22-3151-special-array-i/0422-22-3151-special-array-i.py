class Solution(object):
    def isArraySpecial(self, nums):
        c=0
        for i in range(0,len(nums)-1):
            if nums[i]%2==0:
                if nums[i+1]%2==0:
                    c+=1
                else:
                    c+=0
            if nums[i]%2!=0:
                if nums[i+1]%2!=0:  
                    c+=1
                else:
                    c+=0
        if c==0:
            return True
        else:
            return False
        