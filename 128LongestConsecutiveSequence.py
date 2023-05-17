# Leetcode 128: Longest Consecutive Sequence (medium)
# arrays, sorting

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if nums == []:
            return 0
        
        sorted_nums = sorted(nums)
        counts = [] # list of counts of each sequence
        count = 1 # for the length of each sequence, 1 by default

        for i, n in enumerate(sorted_nums):
            if i + 1 < len(sorted_nums): # if the next item exists (avoid out of range error)
                if n + 1 == sorted_nums[i+1] or n == sorted_nums[i+1]: # if next number is sequential or the same
                    if n == sorted_nums[i+1]: # if next number is the same
                        continue # skip and don't increase the count
                    count += 1 # increment the sequential numbers count
                else: # if next number is not sequential
                    counts.append(count) # append the highest count that was reached
                    count = 1
             # append the count when at the end of the list (resetting is obviously unneeded)
            else: counts.append(count)
        
        # sort the counts in descending order
        sorted_counts = sorted(counts, reverse=True)

        return sorted_counts[0] # return the highest count, this will be the longest consecutive sequence


solution = Solution()
print(solution.longestConsecutive([1, 2, 0, 1]))