class Solution(object):
    def merge(self, a, m, b, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        merge1 = []
        i=0 
        j=0  
        while i<m and j < n:
            if a[i] > b[j] :
                    merge1.append(b[j])
                    j+=1
            else:
                merge1.append(a[i])
                i+=1

        while i< m:
            merge1.append(a[i])
            i+=1

        while j< n:
            
            merge1.append(b[j])
            j+=1
        for i in range(len(merge1)):
            a[i] = merge1[i]
        return a