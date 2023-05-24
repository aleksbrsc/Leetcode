# Leetcode 1929. Concatenation of Array (easy)
# array

class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return nums * 2

# test cases
solution = Solution()
print(solution.getConcatenation([1,2,1]))
print(solution.getConcatenation([1,3,2,1]))