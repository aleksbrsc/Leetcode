# Leetcode 1431. Kids With the Greatest Number of Candies (easy)
# array
class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        result = []
        highest = max(candies)

        for c in candies:
            if c + extraCandies >= highest:
                result.append(True)
            else: result.append(False)

        return result

# test cases
solution = Solution()
candies = [2,3,5,1,3]
extraCandies = 3
print(solution.kidsWithCandies(candies, extraCandies)) # [true,true,true,false,true]
candies = [4,2,1,1,2]
extraCandies = 1
print(solution.kidsWithCandies(candies, extraCandies)) # [true,false,false,false,false]
candies = [12,1,12]
extraCandies = 10
print(solution.kidsWithCandies(candies, extraCandies)) # [true,false,true]