# Leetcode 561. Array Partition (easy)
# array

class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        nums.sort()

        for i in range(0, len(nums), 2):
            ans += nums[i]

        return ans

# test cases
solution = Solution()
nums = [1,4,3,2]
print(solution.arrayPairSum(nums)) # 4
nums = [6,2,6,5,1,2]
print(solution.arrayPairSum(nums)) # 9