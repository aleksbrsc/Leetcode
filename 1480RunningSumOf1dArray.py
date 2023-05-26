# Leetcode 1480. Running Sum of 1d Array (easy, easiest)
# array

# Given an array nums, we define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.

class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sum = 0
        running_sum = []

        for n in nums:
            sum += n
            running_sum.append(sum)
        
        return running_sum

# test cases
solution = Solution()
print(solution.runningSum([1,2,3,4])) # [1,3,6,10]
print(solution.runningSum([1,1,1,1,1])) # [1,2,3,4,5]
print(solution.runningSum([3,1,2,10,1])) # [3,4,6,16,17]