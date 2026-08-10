class Solution:
    def plusOne(self, n: List[int]) -> List[int]:
        sum = 0
        for i in range(0,len(n)):
            sum = sum*10 + n[i]
        b = sum+1
        l = []
        while  b > 0:
            id = b%10
            l.append(id)
            b//=10
        return l[::-1]
