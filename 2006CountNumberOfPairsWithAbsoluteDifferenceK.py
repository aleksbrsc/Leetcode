# Leetcode 2006. Count Number of Pairs With Absolute Difference K (easy)
# array

class Solution(object):
    def countKDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0

        for i, n in enumerate(nums):
            for j, m in enumerate(nums):
                if i < j and abs(n - m) == k:
                    count += 1
        
        return count
                    

# test cases
solution = Solution()
nums = [1,2,2,1]
k = 1
print(solution.countKDifference(nums, k)) # 4