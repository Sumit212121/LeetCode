class Solution:
    def findLonely(self, a: List[int]) -> List[int]:
        d = {}
        for i in range(0,len(a)):
            if a[i] in d :
                d[a[i]] += 1
            else:
                d[a[i]] = 1

        l = []
        for key,value in d.items():
            if value == 1:
                if key-1 not in d and key+1 not in d:
                    l.append(key)
        return l