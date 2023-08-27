# Leetcode 347: Top K Frequent Elements
# arrays, hashing


# from collections import defaultdict
class Solution:
    def topKFrequent(self, nums, k):
        freq, ans = {}, []
        for n in nums:
            if n in freq: freq[n] += 1
            else: freq[n] = 1
        
        sorted_freq = sorted(freq.items(), key=lambda x:x[1], reverse=True)

        for i in range(k):
            ans.append(sorted_freq[i][0])
        
        return ans

solution = Solution()
nums = [1,1,1,2,2,3]
k = 2
print(solution.topKFrequent(nums, k)) # [1,2]
print(solution.topKFrequent([1], 1)) # [1]


# LEETCODE 347 TESTCASES NOT WORKING CORRECTLY, BUT THE EXACT TESTCASE WORKS HERE? see bottom
    # def topKFrequent2(self, nums: list[int], k: int) -> list[int]:
    #     count_map = defaultdict(list) # number : count
    #     result = []

    #     # appending each number and the amount of times it appears to the count map
    #     for n in nums:
    #         if count_map[n]: # if the value is not null / already exists
    #             count_map[n] = count_map[n] + 1 # increment the count value
    #         else: 
    #             count_map[n] = 1 # set the count to 1
        
    #     # sort hashmap by its values in reverse order, basically its count in descending order
    #     # sorted returns a list therefore cast back to defaultdict
    #     sorted_count_map = dict(sorted(count_map.items(), key=lambda x:x[1], reverse=True))

    #     # append the sorted keys to the result list until k amount is reached
    #     for i, key in enumerate(sorted_count_map):
    #         if i < k:
    #             result.append(key)
            
    #     return result
