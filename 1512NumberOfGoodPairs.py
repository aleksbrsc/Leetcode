# Leetcode 1512. Number of Good Pairs (easy)
# array

# Given an array of integers nums, return the number of good pairs.
# A pair (i, j) is called good if
# nums[i] == nums[j]   and    i < j.

class Solution(object):
    # with enumerate (50% faster)
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0

        for i, n in enumerate(nums):
            j = 0
            while j < len(nums):
                if n == nums[j] and i < j:
                    count += 1
                j += 1
        
        return count
    
    # without enumerate (5% faster)
    def numIdenticalPairs2(self, nums):
        count = 0
        i = 0

        while i < len(nums):
            j = 0
            while j < len(nums):
                if nums[i] == nums[j] and i < j:
                    count += 1
                j += 1
            i += 1
        
        return count

# test cases
solution = Solution()
print(solution.numIdenticalPairs([1,2,3,1,1,3])) # 4
print(solution.numIdenticalPairs([1,1,1,1])) # 6
print(solution.numIdenticalPairs([1,2,3])) # 0
