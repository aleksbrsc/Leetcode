# Leetcode 821. Shortest Distance to a Character (easy)
# array, string

class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        ans, char_indices = [], []

        for i, substring in enumerate(s):
            if substring == c:
                char_indices.append(i)

        for i, substring in enumerate(s):
            if substring == c:
                ans.append(0)
                continue
            closest = len(s)
            for j in char_indices:
                nearby = abs(i - j)
                if nearby < closest:
                    closest = nearby
            ans.append(closest)
            
        return ans
            



# test cases
solution = Solution()
s = "loveleetcode"
c = "e"
print(solution.shortestToChar(s, c)) # [3,2,1,0,1,0,0,1,2,2,1,0]
s = "aaab"
c = "b"
print(solution.shortestToChar(s, c)) # [3,2,1,0]