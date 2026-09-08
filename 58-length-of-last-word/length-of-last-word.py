class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = s.split(" ")
        for i in range(len(a)-1,-1,-1):
            if a[i]=="":
                continue
            else:
                return len(a[i])
            