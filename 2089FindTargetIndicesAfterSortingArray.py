# Leetcode 2089. Find Target Indices After Sorting Array (easy)
# array

class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ans = []

        for i, n in enumerate(sorted(nums)):
            if n == target: ans.append(i)
        
        return ans

# test cases
solution = Solution()
nums = [1,2,5,2,3]
target = 2
print(solution.targetIndices(nums, target)) # [1,2]
nums = [1,2,5,2,3]
target = 3
print(solution.targetIndices(nums, target)) # [3]
nums = [1,2,5,2,3]
target = 5
print(solution.targetIndices(nums, target)) # [4]