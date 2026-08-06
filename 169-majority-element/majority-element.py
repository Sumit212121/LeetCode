class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d ={}
        for i in range(0,len(nums)):
            if nums[i] in d:
                d[nums[i]] +=1
            else:
                d[nums[i]] =1
        max_freq = 0
        for key,value in d.items():
            if value > max_freq:
                max_freq = value
        if max_freq > len(nums)//2:
            for key,value in d.items():
                if value == max_freq:
                    return key
        else :
            return -1