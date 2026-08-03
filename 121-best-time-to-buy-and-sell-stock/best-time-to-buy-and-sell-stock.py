class Solution(object):
    def maxProfit(self, a):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_num = a[0]
        max_pro = 0
        for i in range(1,len(a)):
            if a[i] < min_num:
                min_num= a[i]
            if a[i] - min_num > max_pro:
                max_pro = a[i]-min_num
        return max_pro