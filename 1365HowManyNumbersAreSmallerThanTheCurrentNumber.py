# Leetcode 1365. How Many Numbers Are Smaller Than the Current Number (easy)
# array

class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []

        for i, current in enumerate(nums):
            smaller = 0
            for j, other in enumerate(nums):
                if i != j and current > other:
                    smaller += 1
            result.append(smaller)

        return result
        
# test cases
solution = Solution()
print(solution.smallerNumbersThanCurrent([8,1,2,2,3])) # [4,0,1,1,3]
print(solution.smallerNumbersThanCurrent([6,5,4,8])) # [2,1,0,3]
print(solution.smallerNumbersThanCurrent([7,7,7,7])) # [0,0,0,0]