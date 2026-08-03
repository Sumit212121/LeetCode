class Solution:
    def findKthPositive(self, nums: List[int], k: int) -> int:
        i = 1
        l = []

        while len(l) < k:
            if i not in nums:
                l.append(i)
            i += 1

        return l[k - 1]