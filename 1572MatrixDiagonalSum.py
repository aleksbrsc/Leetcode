# Leetcode 1572. Matrix Diagonal Sum (easy)
# array

class Solution(object):
    # can rewrite this to be more condensed
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        diagonals_sum, i = 0, 0

        while i < len(mat):
            diagonals_sum += mat[i][i] + mat[i][len(mat) -1 - i]
            i += 1

        if len(mat) % 2 != 0:
            middle = (len(mat) // 2)
            diagonals_sum -= mat[middle][middle]

        return diagonals_sum

# test cases
solution = Solution()
mat = [[1,2,3],
    [4,5,6],
    [7,8,9]]
print(solution.diagonalSum(mat)) # 25
mat = [[1,1,1,1],
    [1,1,1,1],
    [1,1,1,1],
    [1,1,1,1]]
print(solution.diagonalSum(mat)) # 8
mat = [[5]]
print(solution.diagonalSum(mat)) # 5
mat = [[7,3,1,9],
       [3,4,6,9],
       [6,9,6,6],
       [9,5,8,5]]
print(solution.diagonalSum(mat)) # 55
