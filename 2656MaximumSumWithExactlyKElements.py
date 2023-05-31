# Leetcode 2656. Maximum Sum With Exactly K Elements (easy)
# array

class Solution(object):
    def maximizeSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        highest = max(nums)
        i, count = 0, 0

        while i < k:
            count += highest + i
            i += 1

        return count
    
    def maximizeSum2(self, nums, k):
        return k * max(nums) + k * (k - 1) // 2
        
# test cases
solution = Solution()
nums = [1,2,3,4,5]
k = 3
print(solution.maximizeSum2(nums, k))
nums = [5,5,5]
k = 2
print(solution.maximizeSum2(nums, k))