# Leetcode 1374: Generate a String With Characters That Have Odd Counts (easy)
# string

class Solution(object):
    # 95% faster
    def generateTheString(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = ""
        odd = n % 2 != 0

        if odd: # xxx ... x
            result += "x" * n
        else:
            result += "x" * (n - 1) + "y"

        return result


# test cases
solution = Solution()
print(solution.generateTheString(5))
print(solution.generateTheString(6))
        