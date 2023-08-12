# Leetcode 2710. Remove Trailing Zeros From a String (easy)
# string

class Solution(object):
    def removeTrailingZeros(self, num):
        """
        :type num: str
        :rtype: str
        """
        trailing = True

        while trailing:
            if num[-1] == "0":
                num = num[:-1]
            else: return num

# test cases
solution = Solution()
num = "51230100"
print(solution.removeTrailingZeros(num)) # "512301"
num = "123"
print(solution.removeTrailingZeros(num)) # "123"