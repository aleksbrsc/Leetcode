# Leetcode 1748. Sum of Unique Elements (easy)
# array

class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        unique = []
        non_unique = []
        ans = 0

        for n in nums:
            if n not in unique: unique.append(n)
            else: non_unique.append(n)

        for n in nums:
            if n not in non_unique: ans += n
        
        return ans

# test cases
solution = Solution()
nums = [1,2,3,2]
print(solution.sumOfUnique(nums)) # 4
nums = [1,1,1,1,1]
print(solution.sumOfUnique(nums)) # 0
nums = [1,2,3,4,5]
print(solution.sumOfUnique(nums)) # 15

