# Leetcode 2154. Keep Multiplying Found Values by Two

class Solution(object):
    # should be faster, set has O(1) lookup time because sets are implemented as hash tables, means membership testing is faster.
    def findFinalValue(self, nums, original):
        nums = set(nums)
        while original in nums:
            original *= 2
        return original
    
    # faster on leetcode?
    def findFinalValue(self, nums, original):
        """
        :type nums: List[int]
        :type original: int
        :rtype: int
        """
        while True:
            if original not in nums:
                return original
            else:
                original *= 2

# test cases
solution = Solution()
nums = [5,3,6,1,12]
original = 3
print(solution.findFinalValue(nums, original)) # 24
nums = [2,7,9]
original = 4
print(solution.findFinalValue(nums, original)) # 4