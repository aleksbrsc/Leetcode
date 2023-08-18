# Leetcode 2103. Rings and Rods (easy)
# hash map

class Solution(object):
    def countPoints(self, rings):
        """
        :type rings: str
        :rtype: int
        """
        ans, i = 0, 0
        rods_map = {}

        while i < len(rings):
            if rings[i+1] not in rods_map:
                rods_map[rings[i+1]] = rings[i]
            else: 
                rods_map[rings[i+1]] += rings[i]
            i += 2

        for rod in rods_map:
            if "R" in rods_map[rod] and "G" in rods_map[rod] and "B" in rods_map[rod]: ans += 1

        return ans

        
        
# test cases
solution = Solution()
rings = "B0B6G0R6R0R6G9"
print(solution.countPoints(rings)) # 1
rings = "B0R0G0R9R0B0G0"
print(solution.countPoints(rings)) # 1
rings = "G4"
print(solution.countPoints(rings)) # 