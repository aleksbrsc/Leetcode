# Leetcode 905. Sort Array By Parity (easy)
# array

class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        odd, even = [], []
        for i in nums:
            if i % 2 == 0: even.append(i)
            else: odd.append(i)

        return even + odd
        
# test cases
solution = Solution()
nums = [3,1,2,4]
print(solution.sortArrayByParity(nums)) # [2,4,3,1]
nums = [0]
print(solution.sortArrayByParity(nums)) # [0]
