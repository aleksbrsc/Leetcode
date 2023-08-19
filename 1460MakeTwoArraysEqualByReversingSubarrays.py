# Leetcode 1460. Make Two Arrays Equal by Reversing Subarrays (easy)
# array, hashmap

class Solution(object):
    def canBeEqual(self, target, arr):
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: bool
        """
        return sorted(target) == sorted(arr)

# test cases
solution = Solution()
target = [1,2,3,4]
arr = [2,4,1,3]
print(solution.canBeEqual(target, arr)) # true
target = [7]
arr = [7]
print(solution.canBeEqual(target, arr)) # true
target = [3,7,9]
arr = [3,7,11]
print(solution.canBeEqual(target, arr)) # false