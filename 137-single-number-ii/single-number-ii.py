class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d= {}
        for i in range(0,len(nums)):
            if nums[i] in d:
                d[nums[i]] +=1
            else:
                d[nums[i]] =1
        for key,value in d.items():
            if value == 1:
                return key