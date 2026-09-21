class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        l1 = []
        for i in s:
            if i != '#':
                l1.append(i)
            else:
                if l1:  # ye check kar raha hai ki list empty to nahi
                    l1.pop()
        s1 = ''.join(l1)
        l2 = []
        for j in t:
            if j != '#':
                l2.append(j)
            else:
                if l2:
                    l2.pop()
        t1 = ''.join(l2)
        return s1==t1