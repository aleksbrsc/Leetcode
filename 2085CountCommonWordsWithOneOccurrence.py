# Leetcode 2085. Count Common Words With One Occurrence (easy)
# string, array

class Solution(object):
    def countWords(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: int
        """
        ans = 0
        occurences1, occurences2 = {}, {}
        
        for word in words1:
            if word not in occurences1: occurences1[word] = 1
            else: occurences1[word] += 1

        for word in words2:
            if word not in occurences2: occurences2[word] = 1
            else: occurences2[word] += 1

        for word in occurences1:
            if occurences1[word] == 1 and word in occurences2:
                if occurences2[word] == 1: ans += 1

        return ans
    
# test cases
solution = Solution()
words1 = ["leetcode","is","amazing","as","is"]
words2 = ["amazing","leetcode","is"]
print(solution.countWords(words1, words2)) # 2
words1 = ["b","bb","bbb"]
words2 = ["a","aa","aaa"]
print(solution.countWords(words1, words2)) # 0