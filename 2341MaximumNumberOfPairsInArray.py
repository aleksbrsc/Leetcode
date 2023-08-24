# Leetcode 2341. Maximum Number of Pairs in Array (easy)
# array

class Solution(object):
    def numberOfPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = [0, 0]
        
        for n in set(nums):
            count = nums.count(n)
            if count == 1:
                ans[1] += 1
            elif count % 2 == 0:
                ans[0] += count // 2
            elif count % 2 != 0:
                ans[0] += (count - 1) // 2
                ans[1] += 1

        return ans
    
# test cases
solution = Solution()
nums = [1,3,2,1,3,2,2]
print(solution.numberOfPairs(nums)) # [3,1]
nums = [1,1]
print(solution.numberOfPairs(nums)) # [1,0]
nums = [0]
print(solution.numberOfPairs(nums)) # [0,1]
