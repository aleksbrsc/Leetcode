# Leetcode 217: Contains Duplicate
# hashmap

class Solution:
    def containsDuplicate3(self, nums: list[int]) -> bool:
        already_seen = {} # using a hashmap, faster search than an array which exceeds time limit

        for i, number in enumerate(nums):
            if number in already_seen:
               return True
            else: 
                # if its not in the hashmap, adds it and its index
                already_seen[number] = i # submission note: making the key the number is faster than making the index the key and checking if number is in already_seen.values() -> which causes time limit exceeded 
        return False
    
    def containsDuplicate2(self, nums: list[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
    
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(nums) != len(set(nums))
    
# test cases
solution = Solution()
print(solution.containsDuplicate([1, 1]))