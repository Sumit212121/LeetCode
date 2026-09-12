class Solution(object):
    def commonFactors(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        i=1
        count = 0
        while i <= a and i <= b:
            if a%i == 0 and b%i == 0:
                count +=1
            i+=1
        return count