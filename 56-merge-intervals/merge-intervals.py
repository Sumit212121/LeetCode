class Solution(object):
    def merge(self, n):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        n.sort(key = lambda x:x[0])
        i=1
        while i < len(n):
            if n[i][0] <= n[i-1][1]:
                n[i-1][0] = min(n[i-1][0], n[i][0])
                n[i-1][1] = max(n[i-1][1],n[i][1])

                n.pop(i)
            else:
                i = i+1
        return n