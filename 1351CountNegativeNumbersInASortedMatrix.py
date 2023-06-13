# Leetcode 1351. Count Negative Numbers in a Sorted Matrix (easy)
# array

class Solution(object):
    # O(n * m)
    # note to self: better to use num instead of col for matrices
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ans = 0

        for row in grid:
            for col in row:
                if col < 0: ans += 1

        return ans
    
    def countNegatives2(self, grid):
        return sum(col < 0 for row in grid for col in row)
    
    # optimal O(n + m) solution
    def countNegatives3(self, grid):
        col = m = len(grid[0])
        negative_count = 0

        for row in grid:
            while 0 < col and row[col - 1] < 0:
                col -= 1
            negative_count += m - col

        return negative_count

# test cases
solution = Solution()
grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
print(solution.countNegatives(grid)) # 8
grid = [[3,2],[1,0]]
print(solution.countNegatives(grid)) # 0
