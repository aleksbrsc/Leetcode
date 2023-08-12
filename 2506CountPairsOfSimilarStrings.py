# Leetcode 2506. Count Pairs Of Similar Strings (easy)
# string

class Solution(object):
    def similarPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        ans = 0

        for i, word in enumerate(words):
            for j in range(i+1, len(words)):
                if sorted(set(word)) == sorted(set(words[j])): ans += 1
        
        return ans


# test cases
solution = Solution()
words = ["aba","aabb","abcd","bac","aabc"]
print(solution.similarPairs(words)) # 2
words = ["aabb","ab","ba"]
print(solution.similarPairs(words)) # 3
words = ["nba","cba","dba"]
print(solution.similarPairs(words)) # 0