# Leetcode 2357. Make Array Zero by Subtracting Equal Amounts (easy)
# array, hashmap

class Solution(object):
    # fastest approach
    def minimumOperations(self, nums):
        return len(set(nums) - {0})
    
    # slow first approach
    def minimumOperations2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        while True:
            lowest = max(nums)
            for n in nums:
                if n > 0 and n < lowest:
                    lowest = n

            if lowest == 0: return ans

            for i, n in enumerate(nums):
                nums[i] = (n - lowest)

            ans += 1

# test cases
solution = Solution()
nums = [1,5,0,3,5]
print(solution.minimumOperations(nums)) # 3
"""
In the first operation, choose x = 1. Now, nums = [0,4,0,2,4].
In the second operation, choose x = 2. Now, nums = [0,2,0,0,2].
In the third operation, choose x = 2. Now, nums = [0,0,0,0,0].
"""
nums = [0]
print(solution.minimumOperations(nums)) # 0
"""Each element in nums is already 0 so no operations are needed."""
