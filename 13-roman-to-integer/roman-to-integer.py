class Solution(object):
    def romanToInt(self, a):
        """
        :type s: str
        :rtype: int
        """
        d = {'I':1,'V':5, 'X':10,'L':50,'C':100,'D':500,'M':1000}
        sum = 0
        for i in range(len(a)):
            current = d[a[i]]
            if i+1 < len(a):
                next = d[a[i+1]]

                if current <next :
                    sum = sum - current
                else:
                    sum = sum + current
            else:
                sum = sum + current
        return sum