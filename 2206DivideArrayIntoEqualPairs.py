# Leetcode 2206. Divide Array Into Equal Pairs (easy)
# array

class Solution(object):
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()

        for i in range(0, len(nums), 2):
            if nums[i] != nums[i+1]: return False

        return True

# test cases
solution = Solution()
print(solution.divideArray([3,2,3,2,2,2])) # true
print(solution.divideArray([1,2,3,4])) # false