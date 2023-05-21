# Leetcode 2418: Sort the People (easy)
# string, hashmap
from collections import defaultdict
class Solution(object):
    # works everywhere else besides leetcode, does leetcode interpreter not like defaultdict?
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        people = defaultdict(list)

        for i, n in enumerate(names):
            people[n] = heights[i]
        
        ordered = dict(sorted(people.items())[::-1]) # slice notation but can use reverse=True inside sorted method

        return ordered.keys()
    
    # works on leetcode, zip function quickly maps two lists together
    def sortPeople2(self, names, heights):
        ordered = []
        height_map = dict(zip(heights, names))

        for height in sorted(height_map.keys())[::-1]: 
            ordered.append(height_map[height])

        return ordered
    
# test cases
solution = Solution()
names = ["Mary","John","Emma"]
heights = [180,165,170]
print(solution.sortPeople(names, heights))
        
