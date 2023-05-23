# Leetcode 1812: Determine Color of a Chessboard Square (easy)
# string

class Solution(object):
    def squareIsWhite(self, coordinates):
        """
        :type coordinates: str
        :rtype: bool
        """
        print(((ord(coordinates[0]) - 96) + int(coordinates[1])) % 2)
        return not ((ord(coordinates[0]) - 96) + int(coordinates[1])) % 2 == 0

# test cases
solution = Solution()
print(solution.squareIsWhite("h3"))