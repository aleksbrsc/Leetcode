# Leetcode 238. Product of Array Except Self (medium)
# array

class Solution(object):
    def productExceptSelf(self, nums):
        ans = [1] * len(nums) 

        prefix, postfix = 1, 1
        for i in range(len(nums)):
            ans[i] = prefix
            prefix *= nums[i]
        for i in range(len(nums)-1, -1, -1):
            ans[i] *= postfix
            postfix *= nums[i]

        return ans

    def productExceptSelf2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            ans[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            ans[i] *= postfix
            postfix *= nums[i]

        return ans

# test cases
solution = Solution()
nums = [1,2,3,4]
print(solution.productExceptSelf(nums)) # [24,12,8,6]
nums = [-1,1,0,-3,3]
print(solution.productExceptSelf(nums)) # [0,0,9,0,0]
