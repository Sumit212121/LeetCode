class Solution:
    def isFascinating(self, a: int) -> bool:
        s = str(a)
        b = str(2*a)
        c = str(3*a)
        con = s+b+c
        print(con)
        d = {}
        for i in range(0,len(con)):
            if con[i] == '0':
                return False
            if con[i] in '123456789':
                if con[i] in d: 
                    return False
                else:
                    d[con[i]] = 1
        return True