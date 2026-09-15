class Solution(object):
    def isPalindrome(self, n):
        """
        :type s: str
        :rtype: bool
        """
        a = []
        for i in n:
            if 'A'<= i <= "Z" or 'a' <= i <= 'z' or '0' <= i <= '9':
                a.append(i.lower())
        s = "".join(a)
        left = 0
        right = len(s) -1
        while left < right:
            if s[left] != s[right]:
                return False
            left +=1
            right -=1
        return True