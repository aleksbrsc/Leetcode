# Leetcode 1684: Count the Number of Consistent Strings (easy)
# string

class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        count = 0

        for word in words:
            if any(char not in allowed for char in word):
                continue
            count += 1

        return count
    
    # another solution using a set, but slower than the last one
    def countConsistentStrings2(self, allowed, words):
        count = 0

        for word in words:
            if set(word).difference(allowed):
                continue
            count += 1

        return count
    
# test cases
solution = Solution()
allowed = "ab"
words = ["ad","bd","aaab","baa","badab"]
print(solution.countConsistentStrings(allowed, words))
            