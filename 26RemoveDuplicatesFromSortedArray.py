# Leetcode 26. Remove Duplicates from Sorted Array (easy, flawed description)
# array

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums[:] = sorted(set(nums)) # [:] replaces the elements in place, 
        return len(nums)

# test cases
solution = Solution()
nums = [1,1,2]
print(solution.removeDuplicates(nums))
nums = [0,0,1,1,1,2,2,3,3,4]
print(solution.removeDuplicates(nums))