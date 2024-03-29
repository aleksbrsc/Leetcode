# Leetcode 2399. Check Distances Between Same Letters (easy)
# array, string

"""
You are given a 0-indexed string s consisting of only lowercase English letters, where each letter in s 
appears exactly twice. You are also given a 0-indexed integer array distance of length 26.
Each letter in the alphabet is numbered from 0 to 25 (i.e. 'a' -> 0, 'b' -> 1, 'c' -> 2, ... , 'z' -> 25).
In a well-spaced string, the number of letters between the two occurrences of the ith letter is distance[i].
If the ith letter does not appear in s, then distance[i] can be ignored.
Return true if s is a well-spaced string, otherwise return false.
"""

class Solution(object):
    def checkDistances(self, s, distance):
        """
        :type s: str
        :type distance: List[int]
        :rtype: bool
        """
        letters = set(s)
        
        # mapping letters to distances
        for i, letter in enumerate(s):
            if letter in letters:
                for j in range(i + 1, len(s)):
                    if s[j] == letter:
                        if distance[ord(letter) - 97] != abs(i - j) - 1: return False
            letters.discard(letter)

        return True

# test cases
solution = Solution()
s = "abaccb"
distance = [1,3,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
print(solution.checkDistances(s, distance)) # true
"""
Explanation:
- 'a' appears at indices 0 and 2 so it satisfies distance[0] = 1.
- 'b' appears at indices 1 and 5 so it satisfies distance[1] = 3.
- 'c' appears at indices 3 and 4 so it satisfies distance[2] = 0.
Note that distance[3] = 5, but since 'd' does not appear in s, it can be ignored.
Return true because s is a well-spaced string.
"""
s = "aa"
distance = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
print(solution.checkDistances(s, distance)) # false