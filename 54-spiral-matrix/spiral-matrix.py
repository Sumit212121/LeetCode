class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        if not matrix or not matrix[0]:
            return []
        result = []

        # initialize pointers for traversal
        left = 0
        top = 0
        right =len(matrix[0])-1
        bottom = len(matrix) -1
        # traverse matrix in spiral order
        while top <= bottom  and left <= right:
            #move left to right across the top row
            for i in range(left,right+1):
                result.append(matrix[top][i])
            top += 1
            #MOVE top to bottom along the right column
            for i in range(top,bottom+1):
                result.append(matrix[i][right])
            right -=1

            # move  right ot left across the buttom row (if still valid)
            if top <= bottom:  # ye jab 1D matrix hoga tab
                for i in range(right,left-1,-1):
                    result.append(matrix[bottom][i])
                bottom -=1
            # move bottom to top along the left column
            if left<=right:
                for i in range(bottom,top-1,-1):
                    result.append(matrix[i][left])
                left += 1
        return result
