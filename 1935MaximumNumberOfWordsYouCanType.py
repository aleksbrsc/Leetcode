# Leetcode 1935. Maximum Number of Words You Can Type (easy)
# string array

class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        words = text.split(" ")
        count = len(words)

        for word in words:
            broken = False
            for char in word:
                if char in brokenLetters and broken == False:
                    count -= 1
                    broken = True

        return count
    
    # faster, changed the order of broken flag conditional
    def canBeTypedWords2(self, text, brokenLetters):
        words = text.split(" ")
        count = len(words)

        for word in words:
            broken = False
            for char in word:
                if broken == True: continue
                if char in brokenLetters:
                    count -= 1
                    broken = True

        return count

# test cases
solution = Solution()
text = "hello world"
brokenLetters = "ad"
print(solution.canBeTypedWords(text, brokenLetters)) # 1
text = "leet code"
brokenLetters = "lt"
print(solution.canBeTypedWords(text, brokenLetters)) # 1
text = "leet code"
brokenLetters = "e"
print(solution.canBeTypedWords(text, brokenLetters)) # 0