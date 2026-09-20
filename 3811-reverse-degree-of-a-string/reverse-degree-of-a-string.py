class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0
        for i in range(0,len(s)):
            char = s[i]
            reverse = 26 - (ord(char) - ord("a"))

            position = i+1
            total += reverse*position

        return total