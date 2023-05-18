# Leetcode 1528: Shuffle String (easy)
# string, hashmap

from collections import defaultdict
class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        # if args empty then return empty string
        if s == "" or indices == []: 
            return ""

        shufflemap = defaultdict(list) # maps shuffled position : character
        shuffled = "" # the shuffled string to be returned

        for i, c in enumerate(s):
            index = indices[i] # new index
            shufflemap[index].append(c) # append to the shufflemap new index : char 

        for i in range(len(s)):
            shuffled += shufflemap[i].pop() # append char according to its new index, then remove it from the shuffle map

        return shuffled # return the shuffled string

    # simpler and faster solution without hashmap
    def restoreStringSimpler(self, s, indices):
        shuffled = ""

        for i in range(len(indices)):
            shuffled += s[indices.index(i)] # first get the value corresponding to the index -> this is the new index. Then retrieve the character with that new index and append it to the shuffled string

        return shuffled
            
# test cases
solution = Solution()
indices = [4,5,6,7,0,2,1,3]
print(solution.restoreString("codeleet", indices))
print(solution.restoreStringSimpler("codeleet", indices))