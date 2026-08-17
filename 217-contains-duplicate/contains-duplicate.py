class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d = {}
        for i in range(0,len(nums)):
            if nums[i] in d:
                d[nums[i]] +=1
            else:
                d[nums[i]] =1
        
        for k,v in d.items():
            if v > 1:
                return True
        return False
        