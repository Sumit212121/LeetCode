class Solution(object):
    def isAnagram(self, n, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s={}
        if len(n)!=len(t):
            return False
        for i in range(0,len(n)):
            if n[i] in s:
                s[n[i]]+=1
            else:
                s[n[i]]=1
        for j in t:
            if j not in s:
                return False
            else:
                if s[j]==0:
                    return False
                else:
                    s[j]-=1
        return True 
        