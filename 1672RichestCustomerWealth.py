# Leetcode 1672. Richest Customer Wealth (easy)
# array

class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        return max(sum(account) for account in accounts)

# test cases
solution = Solution()
print(solution.maximumWealth([[1,2,3],[3,2,1]])) # 6
print(solution.maximumWealth([[1,5],[7,3],[3,5]])) # 10
print(solution.maximumWealth([[2,8,7],[7,1,3],[1,9,5]])) #17