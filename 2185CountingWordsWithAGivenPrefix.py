# Leetcode 2185: Counting Words With a Given Prefix (easy)
# string

class Solution(object):
    def prefixCount(self, words, pref):
        """
        :type words: List[str]
        :type pref: str
        :rtype: int
        """
        count = 0

        for word in words:
            pref_count = 0
            if len(pref) <= len(word):
                for i in range(len(pref)):
                    if word[i] == pref[i]:
                        pref_count += 1
                    if pref_count == len(pref):
                        count += 1

        return count
    
    # top one line solution
    def prefixCount2(self, words, pref):
        return sum([word.startswith(pref) for word in words])
    
# test cases
solution = Solution()
words = ["pay","attention","practice","attend"]
pref = "at"
print(solution.prefixCount(words, pref))
words = ["leetcode","win","loops","success"]
pref = "code"
print(solution.prefixCount(words, pref))