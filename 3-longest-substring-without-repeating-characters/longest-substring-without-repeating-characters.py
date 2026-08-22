class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        index = [-1] * 128
        left = 0
        max_len = 0
        for right in range(len(s)):
            ch = s[right]

            if index[ord(ch)] >= left :
                left = index[ord(ch)] +1

            index[ord(ch)] = right
            length = right - left +1
            if length > max_len:
                max_len = length
        return max_len