class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        d = {}
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]] +=1
            else:
                d[nums[i]] = 1
        n =len(nums)
        l =[]
        a = n//3
        for k,v in d.items():
            if v > a:
                l.append(k)
        return l