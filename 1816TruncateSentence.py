# Leetcode 1816: Truncate Sentence (easy)
# string

class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        words = s.split()
        truncated = ""
        
        for i in range(k):
            truncated += words[i] + " "

        return truncated[:-1]
    
    # top rated one line solution
    def truncateSentence2(self, s, k):
        return " ".join(s.split()[:k])
    
# test cases
solution = Solution()
s = "Hello how are you Contestant"
k = 4
print(solution.truncateSentence(s, k))
print(solution.truncateSentence2(s, k))
