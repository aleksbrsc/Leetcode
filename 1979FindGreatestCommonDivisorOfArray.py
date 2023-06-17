# Leetcode  1979. Find Greatest Common Divisor of Array (easy)
# array

class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(min(nums), 0, -1):
            if min(nums) % i == 0 and max(nums) % i == 0:
                return i

# test cases
solution = Solution()
nums = [2,5,6,9,10]
print(solution.findGCD(nums)) # 2
nums = [7,5,6,8,3]
print(solution.findGCD(nums)) # 1
nums = [3,3]
print(solution.findGCD(nums)) # 3