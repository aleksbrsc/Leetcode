# Leetcode 2744. Find Maximum Number of String Pairs (easy)
# array, string

class Solution(object):
    def maximumNumberOfStringPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        used = []

        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                if words[i] == words[j][::-1]:
                    used.append(words[i])
                    used.append(words[j])
        
        return len(used) // 2


        

# test cases
solution = Solution()
words = ["cd","ac","dc","ca","zz"]
print(solution.maximumNumberOfStringPairs(words)) # 2
words = ["ab","ba","cc"]
print(solution.maximumNumberOfStringPairs(words)) # 1
words = ["aa","ab"]
print(solution.maximumNumberOfStringPairs(words)) # 0