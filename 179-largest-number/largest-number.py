class Solution:
    def largestNumber(self, nums):

        # Numbers ko string banao
        for i in range(len(nums)):
            nums[i] = str(nums[i])

        # Nested loop sorting
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):

                if nums[i] + nums[j] < nums[j] + nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]

        ans = ''

        for i in nums:
            ans += i

        if ans[0] == '0':
            return '0'

        return ans