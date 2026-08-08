class Solution:
    def SumOfDigits(self, num):
        summ = 0

        for i in str(num):
            summ += int(i)

        return summ

    def addDigits(self, num):
        while len(str(num)) != 1:
            num = Solution.SumOfDigits(self, num)

        return num