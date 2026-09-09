class Solution(object):
    def maxArea(self, a):
        """
        :type height: List[int]
        :rtype: int
        """
        start = 0
        end = len(a) - 1
        max_area = 0
        while start < end:
            area = 0
            if a[start] < a[end]:
                area =(end - start) * a[start]
                start +=1
            else:
                area = (end - start) *a[end]
                end -=1
            if area > max_area:
                max_area = area
        return max_area