class Solution:
    def removeDuplicates(self, a: List[int]) -> int:
        d = {}
        for i in range(0,len(a)):
            if a[i] in d : 
                d[a[i]] +=1
            else:
                d[a[i]] =1
        print(d)
        nz = len(d)
        key = list(d.keys())
        for i in range(0,nz):
            a[i] = key[i]
        for i in range(nz,len(a)):
            a[i] = "_"
        return nz