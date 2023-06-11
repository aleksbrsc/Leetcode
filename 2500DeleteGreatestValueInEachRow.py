# Leetcode 2500. Delete Greatest Value in Each Row (easy)
# array, matrix

class Solution(object):
    def deleteGreatestValue(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count = 0
        sorted_grid = [sorted(row, reverse=True) for row in grid]
        
        for i in range(len(grid[0])):
            greatest = 0
            for row in sorted_grid:
                if row[i] > greatest:
                    greatest = row[i]
            count += greatest
        
        return count

# test cases
solution = Solution()
grid = [[1,2,4],[3,3,1]]
print(solution.deleteGreatestValue(grid)) # 8
grid = [[10]]
print(solution.deleteGreatestValue(grid)) # 10