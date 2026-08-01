class Solution:
    def leftRightDifference(self, a: List[int]) -> List[int]:
        left_sum = []
        sum = 0
        for i in a:
            left_sum.append(sum)
            sum = sum + i

        right_sum = []
        sum1 = 0
        for i in range(len(a)-1,-1,-1):
            right_sum.append(sum1)
            sum1 += a[i]
        right_sum.reverse()
        result =[]
        for i in range(len(left_sum)):
            result.append(abs(left_sum[i] - right_sum[i]))
        return result