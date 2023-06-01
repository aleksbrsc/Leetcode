# Leetcode 1913. Maximum Product Difference Between Two Pairs (easy)
# array

class Solution(object):
    def maxProductDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        w, x, y, z = nums[-1], nums[-2], nums[0], nums[1]
        return (w * x) - (y * z)
    
    # O(nlogn) time O(1) space
    def maxProductDifference2(self, nums):
        nums.sort()
        return (nums[-1] * nums[-2]) - (nums[0] * nums[1])
    
    # O(n) time O(1) space solution i found without sort
    def maxProductDifference3(self, nums: list[int]) -> int:
        min1 = min2 = float('inf')
        max1 = max2 = float('-inf')
        for n in nums:
            if n <= min1:
                min1, min2, = n, min1
            elif n < min2:
                min2 = n
            if n >= max1:
                max1, max2 = n, max1
            elif n > max2:
                max2 = n
        return max1*max2-min1*min2

# test cases
solution = Solution()
print(solution.maxProductDifference([5,6,2,7,4])) # 34
print(solution.maxProductDifference([4,2,5,9,7,4,8])) # 64