class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for i in range(0,len(words)):
            if self.is_prime(words[i]):
                return words[i]
        return ""
    
    def is_prime(self,n):
        left = 0
        right = len(n)-1
        while left < right:
            if n[left] == n[right]:
                left +=1
                right -=1
            else:
                return False
        return True
        