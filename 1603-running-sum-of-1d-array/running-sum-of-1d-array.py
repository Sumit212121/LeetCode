class Solution(object):
    def runningSum(self, a):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(1,len(a)):
            a[i] = a[i]+a[i-1]
        return a