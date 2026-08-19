class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        d= {}
        for i in range(0,len(nums)):
            if nums[i] in d:
                d[nums[i]] +=1
            else:
                d[nums[i]] =1
        l=[]
        for key,value in d.items():
            if value == 1:
                l.append(key)
        sum = 0
        for i in l:
            sum+=i
        return sum
                