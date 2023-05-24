# Leetcode 1920. Build Array from Permutation (easy)
# array

class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        i = 0

        while i < len(nums):
            ans.append(nums[nums[i]])
            i += 1

        return ans

# test cases
solution = Solution()
print(solution.buildArray([0,2,1,5,3,4])) # [0,1,2,4,5,3]
print(solution.buildArray([5,0,1,2,3,4])) # [4,5,0,1,2,3]
# print(solution.buildArray())
# print(solution.buildArray())