# Leetcode 2176. Count Equal and Divisible Pairs in an Array (easy)
# array
from collections import defaultdict

class Solution(object):
    def countPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pairs = 0
        n = len(nums)

        for i in range(n):
            for j in range(i, n):
                if i != j and nums[i] == nums[j] and (i * j) % k == 0:
                    pairs += 1

        return pairs
    
    # solution found that makes a hashmap to traverse indices with same values
    def countPairs(self, nums, k):
        cnt, d = 0, defaultdict(list)
        for i, n in enumerate(nums):
            d[n].append(i)
        for indices in d.values():    
            for i, a in enumerate(indices):
                for b in indices[: i]:
                    if a * b % k == 0:
                        cnt += 1
        return cnt
    
# test cases
solution = Solution()
nums = [3,1,2,2,2,1,3]
k = 2
print(solution.countPairs(nums, k)) # 4
nums = [1,2,3,4]
k = 1
print(solution.countPairs(nums, k)) # 0
