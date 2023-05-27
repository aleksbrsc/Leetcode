# Leetcode 2367. Number of Arithmetic Triplets (easy)
# array

class Solution(object):
    # inefficient
    def arithmeticTriplets(self, nums, diff):
        """
        :type nums: List[int]
        :type diff: int
        :rtype: int
        """
        count = 0

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j: continue
                for k in range(len(nums)):
                    if k == j: continue
                    if i < j < k and nums[j] - nums[i] == diff and nums[k] - nums[j] == diff:
                        count += 1
        
        return count

# test cases
solution = Solution()
nums = [0,1,4,6,7,10]
diff = 3
print(solution.arithmeticTriplets(nums, diff))
nums = [4,5,6,7,8,9]
diff = 2
print(solution.arithmeticTriplets(nums, diff))