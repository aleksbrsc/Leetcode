# Leetcode 711: Jewels and Stones (easy, easiest)
# string

class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        count = 0 # number of jewels in the stone

        for char in stones: 
            if char in jewels: # if the character is one of the characters in the jewel string
                count += 1 # add to the count

        return count
    
# test cases
solution = Solution()
print(solution.numJewelsInStones("aA","aAsssAsa"))
