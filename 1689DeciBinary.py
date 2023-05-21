# Leetcode 1689:Partitioning Into Minimum Number Of Deci-Binary Numbers (medium)
# string

class Solution(object):
    def minPartitions(self, n):
        """
        :type n: str
        :rtype: int
        """
        highest_count = 0
        for n in str(n):
            if int(n) > highest_count:
                highest_count = int(n)

        return highest_count
    
    def minPartitionsOneLine(self, n):
        return max(int(i) for i in str(n))
        
# test cases
solution = Solution()
print(solution.minPartitionsOneLine(32))