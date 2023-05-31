# Leetcode 2373. Largest Local Values in a Matrix (easy)
# array

class Solution(object):
    # could have used for loop in range n - 2
    def largestLocal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(grid)
        i, j = 0, 0
        maxLocal = []

        while i < (n - 2):
            column_maxes = []
            while j < (n - 2):
                highest = max(grid[i][j], grid[i+1][j], grid[i+2][j], 
                              grid[i][j+1], grid[i+1][j+1], grid[i+2][j+1],
                              grid[i][j+2], grid[i+1][j+2], grid[i+2][j+2])
                column_maxes.append(highest)
                j += 1
            maxLocal.append(column_maxes)
            j = 0
            i += 1

        return maxLocal

# test cases
solution = Solution()
grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]
print(solution.largestLocal(grid)) # [[9,9],[8,6]]
grid = [[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]
print(solution.largestLocal(grid)) # [[2,2,2],[2,2,2],[2,2,2]]