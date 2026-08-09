class Solution(object):
    def kthFactor(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        l = []
        i = 1
        while i <= n:
            if n%i == 0:
                l.append(i)
            i+=1
        for i in range(0,len(l)):
            if i == k-1:
                return l[i]
        return -1