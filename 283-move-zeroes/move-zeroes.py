class Solution(object):
    def moveZeroes(self, a):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l = []
        for i in range(len(a)-1,-1,-1):
            if a[i] == 0:
                b = a.pop(i)
                l.append(b) 
        a.extend(l)
        return a