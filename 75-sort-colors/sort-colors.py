class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        temp0= []
        temp1 = []
        for i in range(0,n):
            if nums[i] == 0:
                temp0.append(nums[i])
            elif nums[i] == 1:
                temp1.append(nums[i])
        nz =len(temp0)
        for i in range(0,nz):
            nums[i]= temp0[i]
        ny = len(temp1)
        for i in range(0,ny):
            nums[nz+i] = temp1[i]
        for j in range(nz+ny,n):
            nums[j]= 2
        return nums