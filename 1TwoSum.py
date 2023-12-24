# Leetcode 1: TwoSum (easy)
# hashmap

class Solution:
    # # brute force solution that returns the numbers 
    # def twoSum(self, nums: list[int], target: int) -> list[int]:
    #     i = 0
    #     for x in nums:
    #         for y in nums:
    #             if nums[i] != y:
    #                 if x + y == target:
    #                     pair = [x, y]
    #                     return pair
    #         i += 1
    #     return ["None"]
    
    # correct way using hashmap which returns the indices
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        prevMap = {} # maps val : index for each previous element
        # i is the index
        # n is the value
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return ["None"]

# test cases
solution = Solution()
set = [2,7,11,15]
target = 9
print(solution.twoSum(set, target)) # [0, 1]