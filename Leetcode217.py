# Leetcode 217: Contains Duplicate
# hashmap

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        already_seen = {}

        for i, number in enumerate(nums):
            if number in already_seen:
               return True
            else: 
                already_seen[number] = i
        return False
    
solution = Solution()
print(solution.containsDuplicate([1, 1]))