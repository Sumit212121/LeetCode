class Solution:

    def expand(self, s, start, end):

        while start >= 0 and end < len(s) and s[start] == s[end]:
            start -= 1
            end += 1

        return s[start + 1:end]

    def longestPalindrome(self, s: str) -> str:

        ans = ""

        for i in range(len(s)):

            p1 = self.expand(s, i, i)

            p2 = self.expand(s, i, i + 1)

            if len(p1) > len(ans):
                ans = p1

            if len(p2) > len(ans):
                ans = p2

        return ans