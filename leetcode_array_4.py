class Solution:
    def isToeplitzMatrix(self, matrix: list[list[int]]) -> bool:
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i][j]!=matrix[i-1][j-1]:
                    return False
        return True
s = Solution()
print(s.isToeplitzMatrix([[1,2,3],[5,1,2],[9,5,1]]))