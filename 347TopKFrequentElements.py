# Leetcode 347: Top K Frequent Elements
# arrays, hashing

# LEETCODE 347 TESTCASES NOT WORKING CORRECTLY, BUT THE EXACT TESTCASE WORKS HERE? see bottom

from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count_map = defaultdict(list) # number : count
        result = []

        # appending each number and the amount of times it appears to the count map
        for n in nums:
            if count_map[n]: # if the value is not null / already exists
                count_map[n] = count_map[n] + 1 # increment the count value
            else: 
                count_map[n] = 1 # set the count to 1
        
        # sort hashmap by its values in reverse order, basically its count in descending order
        # sorted returns a list therefore cast back to defaultdict
        sorted_count_map = dict(sorted(count_map.items(), key=lambda x:x[1], reverse=True))

        # append the sorted keys to the result list until k amount is reached
        for i, key in enumerate(sorted_count_map):
            if i < k:
                result.append(key)
            
        return result

solution = Solution()

leetcodetest = [4,1,-1,2,-1,2,3]

print(solution.topKFrequent([2, 2, 2, 2, 1, 3, 4, 5, 3], 3))
print(solution.topKFrequent(leetcodetest, 2))
