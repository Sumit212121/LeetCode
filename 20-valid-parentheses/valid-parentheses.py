class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for bracket in s:
            if bracket == '(' or bracket == '[' or bracket == '{':
                stack.append(bracket)
            else:
                if len(stack) == 0:
                    return False
                ch = stack.pop()
                if (
                    (bracket == ')' and ch == '(')
                    or (bracket == ']' and ch == '[')
                    or (bracket == '}' and ch == '{')
                    ):
                        continue
                else:
                    return False
        return len(stack) == 0
        
        

# 1. if bracket doesnt match [false]
# 2. at the end ,stack is not empty[false]
# 3. if you find closing,but stack is empty [false]