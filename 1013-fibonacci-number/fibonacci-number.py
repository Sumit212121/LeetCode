class Solution(object):
    def fib(self, n):
        if  n == 0 or n == 1:
            return n
        a = 0
        b= 1
        i=2
        while i<=n:
            c=a+b
            a=b
            b=c
            i+=1
        return c
        
        