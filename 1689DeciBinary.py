# Leetcode 1689:Partitioning Into Minimum Number Of Deci-Binary Numbers (medium)
# string

# basically just return the max digit, heres an explanation I found for it:
    # Assume max digit in n is x.
    # Because deci-binary only contains 0 and 1,
    # we need at least x numbers to sum up a digit x.

    # Now we contruct an answer,
    # Take n = 135 as an example,
    # we initilize 5 deci-binary number with lengh = 3,
    # a1 = 000
    # a2 = 000
    # a3 = 000
    # a4 = 000
    # a5 = 000

    # For the first digit, we fill the first n[0] number with 1
    # For the second digit, we fill the first n[1] number with 1
    # For the third digit, we fill the first n[2] number with 1

    # So we have
    # a1 = 111
    # a2 = 011
    # a3 = 011
    # a4 = 001
    # a5 = 001

    # Finally, we have 111+11+11+1+1=135.

class Solution(object):
    def minPartitions(self, n):
        """
        :type n: str
        :rtype: int
        """
        highest_count = 0
        for n in n:
            if int(n) > highest_count:
                highest_count = int(n)

        return highest_count
    
    def minPartitionsOneLine(self, n):
        return max(int(i) for i in n)
        
# test cases
solution = Solution()
print(solution.minPartitions("829124")) # 9
print(solution.minPartitionsOneLine("32")) # 3
print(solution.minPartitionsOneLine("324")) # 4