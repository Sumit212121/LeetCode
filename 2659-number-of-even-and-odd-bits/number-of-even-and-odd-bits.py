class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        binary = ""
        while n > 0:
            res = n % 2
            binary = str(res) + binary
            n = n//2
        binary = binary[::-1]
        even = 0
        odd = 0
        for i in range(len(binary)-1,-1,-1):
            if i%2==0 and binary[i] == '1':
                even+=1
            elif i%2 != 0 and binary[i] == '1':
                odd+=1
        l =[]
        l.append(even)
        l.append(odd)
        return l