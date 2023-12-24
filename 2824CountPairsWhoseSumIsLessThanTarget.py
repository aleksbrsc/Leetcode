# Leetcode 2824. Count Pairs Whose Sum is Less than Target (easy)
# array, sorting

class Solution:
    def countPairs(self, nums, target):
        ans = 0

        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if (nums[i] + nums[j] < target):
                    ans += 1

        return ans
    
# test cases
solution = Solution()
nums = [-1,1,2,3,1]
target = 2
print(solution.countPairs(nums, target)) # 3
nums = [-6,2,5,-2,-7,-1,3]
target = -2
print(solution.countPairs(nums, target)) # 10