# Leetcode 1464. Maximum Product of Two Elements in an Array (easy)
# array

class Solution(object):
    # inefficient solution
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
 
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if i != j:
                    product = (nums[i] - 1) * (nums[j] - 1)
                    if product > ans:
                        ans = product

        return ans
    
    # realized I can sort, 84% time 95% space
    def maxProduct2(self, nums):
        nums.sort()
        return (nums[-1] - 1) * (nums[-2] - 1)

# test cases
solution = Solution()
nums = [3,4,5,2]
print(solution.maxProduct(nums)) # 12
nums = [1,5,4,5]
print(solution.maxProduct(nums)) # 16
nums = [3,7]
print(solution.maxProduct(nums)) # 12