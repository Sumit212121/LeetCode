class Solution(object):
    def rotate(self, a, k):
        
        n=len(a)
        k = k%n
        temp = a[n-k:]
        for i in range(len(a)-1,k-1,-1):
            a[i] = a[i-k]
        for j in range(k):
            a[j] = temp[j]
        return a