class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        mat  = [[0]*len(matrix) for i in range(len(matrix[0]))]
        for i in range(len(matrix[0])):
            for j in range(len(matrix)):
                mat[i][j]=matrix[j][i]
        return mat
s = Solution()      
print(s.transpose([[1,2,3],[4,5,6],[7,8,9]]))