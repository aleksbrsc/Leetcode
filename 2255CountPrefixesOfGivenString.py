# Leetcode 2255. Count Prefixes of a Given String (easy)
# array

class Solution(object):
    def countPrefixes(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: int
        """
        ans = 0
        
        for word in words:
            if len(word) > len(s): continue
            counter = 0
            for i in range(len(word)):
                if word[i] == s[i]:
                    counter += 1
            if counter == len(word):
                ans += 1

        return ans

# test cases
solution = Solution()
words = ["a","b","c","ab","bc","abc"]
s = "abc"
print(solution.countPrefixes(words, s)) # 3
words = ["a","a"]
s = "aa"
print(solution.countPrefixes(words, s)) # 2
