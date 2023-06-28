# Leetcode 1051. Height Checker (easy, easiest)
# array

class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        expected = sorted(heights)
        ans = 0

        for i in range(len(heights)):
            if heights[i] != expected[i]: ans += 1

        return ans

# test cases
solution = Solution()
heights = [1,1,4,2,1,3]
print(solution.heightChecker(heights)) # 3
heights = [5,1,2,3,4]
print(solution.heightChecker(heights)) # 5
heights = [1,2,3,4,5]
print(solution.heightChecker(heights)) # 0