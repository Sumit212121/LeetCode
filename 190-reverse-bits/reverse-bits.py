class Solution:
    def reverseBits(self, n: int) -> int:
        result= ""
        while n > 0:
            id = n% 2 
            result = str(id) + result
            n//=2
        
        # 32 bits bana rahehai 
        while len(result) <32:
            result="0" +result
        result = result[::-1]
        result = int(result)
        # binay se int mai kar rahe hai
        power = 0
        decimal = 0
        while result > 0:
            id = result % 10
            decimal = decimal + id*(2**power)
            power +=1
            result //=10
        return decimal