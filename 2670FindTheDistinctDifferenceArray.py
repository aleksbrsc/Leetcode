# Leetcode 2670. Find the Distinct Difference Array (easy)
# array

class Solution(object):
    # made it readable with comments
    def distinctDifferenceArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []

        for i in range(len(nums)):
            distinct_prefixes, distinct_suffixes = [], [] # distinct prefix/suffix elements
            distinct_prefix_elements, distinct_suffix_elements = 0, 0 # the count of distinct prefix/suffix elements
            
            # determining the number of distinct prefixes
            for p in range(0, i + 1):
                if nums[p] not in distinct_prefixes: distinct_prefixes.append(nums[p])
            distinct_prefix_elements = len(distinct_prefixes)
            
            # determining the number of distinct suffixes
            for s in range(i + 1, len(nums)):
                if nums[s] not in distinct_suffixes: distinct_suffixes.append(nums[s])
            distinct_suffix_elements = len(distinct_suffixes)
            
            # appending the distinct difference to the answer array
            ans.append(distinct_prefix_elements - distinct_suffix_elements)
        
        return ans

# test cases
solution = Solution()
nums = [1,2,3,4,5]
print(solution.distinctDifferenceArray(nums)) # [-3,-1,1,3,5]
nums = [3,2,3,4,2]
print(solution.distinctDifferenceArray(nums)) # [-2,-1,0,2,3]