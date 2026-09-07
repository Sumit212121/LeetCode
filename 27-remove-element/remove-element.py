class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        t = nums.copy()
        for i in range(len(t)-1,-1,-1):
            if t[i] == val:
                t.pop(i)
        nz = len(t)
        for i in range(0,nz):
            nums[i] = t[i]
        for i in range(nz,len(nums)):
            nums[i] = '_'
        return nz