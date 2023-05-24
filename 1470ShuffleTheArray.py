# Leetcode 1470. Shuffle The Array (easy)
# array

class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        x = 0
        y = n
        ans = []

        while x < n:
            ans.append(nums[x])
            ans.append(nums[y])
            x += 1
            y += 1

        return ans

# test cases
solution = Solution()
nums = [2,5,1,3,4,7]
n = 3
print(solution.shuffle(nums, n)) # [2,3,5,4,1,7]
nums = [1,2,3,4,4,3,2,1]
n = 4
print(solution.shuffle(nums, n)) # [1,4,2,3,3,2,4,1]
nums = [1,1,2,2]
n = 2
print(solution.shuffle(nums, n))