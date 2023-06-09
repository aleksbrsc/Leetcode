# Leetcode 1732. Find the Highest Altitude (easy)
# array

class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        altitudes = [0]

        for g in gain:
            altitudes.append(g + altitudes[-1])
        
        return max(altitudes)

# test cases
solution = Solution()
gain = [-5,1,5,0,-7]
print(solution.largestAltitude(gain)) # 1
gain = [-4,-3,-2,-1,4,3,2]
print(solution.largestAltitude(gain)) # 0
