class Solution(object):
    def groupAnagrams(self, s):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        for i in range(0,len(s)):
            n = "".join(sorted(s[i]))
            if n in d :
                d[n].append(s[i])
            else:
                d[n] = [s[i]]
        l = []
        for key,val in d.items():
            l.append(val)
        return l