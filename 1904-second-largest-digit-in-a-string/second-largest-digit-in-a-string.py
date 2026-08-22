class Solution:
    def secondHighest(self, n: str) -> int:
        max_val = -1
        sec_max = -1
        for i in range(0,len(n)):
            if n[i] in '1234567890':
                if int(n[i]) > max_val:
                    max_val = int(n[i])
        for i in range(0,len(n)):
            if n[i] in '1234567890':
                if int(n[i]) > sec_max and int(n[i]) != max_val:
                    sec_max = int(n[i])

        return sec_max