class Solution:
    def reverse(self, x: int) -> int:
        if x>0:
            val = self.reverse_num(x)
        else:
            val = -self.reverse_num(abs(x))
        
        if val < -2**31 or val >2**31 -1:
            return 0

        return val
    def reverse_num(self,n):
        sum = 0
        while n>0:
            id = n% 10
            sum = sum*10 +id
            n//= 10
        return sum

