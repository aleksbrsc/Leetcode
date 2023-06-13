# Leetcode 2643. Row With Maximum Ones (easy)
# array

class Solution(object):
    def rowAndMaximumOnes(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        max_ones = 0

        for row in mat:
            temp = 0
            for col in row:
                if col == 1: temp += 1
            if temp > max_ones: max_ones = temp

        for i, row in enumerate(mat):
            if row.count(1) == max_ones:
                return [i, max_ones]

# test cases
solution = Solution()
mat = [[0,1],[1,0]]
print(solution.rowAndMaximumOnes(mat)) # [0,1]
mat = [[0,0,0],[0,1,1]]
print(solution.rowAndMaximumOnes(mat)) # [1,2]
mat = [[0,0],[1,1],[0,0]]
print(solution.rowAndMaximumOnes(mat)) # [1,2]