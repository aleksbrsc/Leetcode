# Leetcode 128: Longest Consecutive Sequence (medium)
# arrays, sorting

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if nums == []:
            return 0
        
        sorted_nums = sorted(nums)
        counts = []
        count = 1

        for i, n in enumerate(sorted_nums):
            if i + 1 < len(sorted_nums):
                if n + 1 == sorted_nums[i+1] or n == sorted_nums[i+1]:
                    if n == sorted_nums[i+1]:
                        continue
                    count += 1
                else:
                    counts.append(count)
                    count = 1
            else: counts.append(count)

        sorted_counts = sorted(counts, reverse=True)

        return sorted_counts[0] 


solution = Solution()
print(solution.longestConsecutive([1, 2, 0, 1]))