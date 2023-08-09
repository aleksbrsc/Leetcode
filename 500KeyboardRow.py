# Leetcode 500. Keyboard Row (easy)
# array, string

class Solution(object):
    def findWords(self, words):
        ans = []

        for word in words:
            word = word.lower()
            broken = False
            belonging = "qwertyuiop"
            if word[0] in any("asdfghjkl"): belonging = "asdfghjkl"
            if word[0] in "zxcvbnm": belonging = "zxcvbnm"
            for letter in words:
                if letter not in belonging: broken = True 
            if broken == False: ans.append(word)

        return ans

    # list comprehension solution
    def findWords2(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        keyboard_rows = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
        ans = []
        
        for word in words:
            if any(all(char.lower() in row for char in word) for row in keyboard_rows):
                ans.append(word)
        
        return ans

# test cases
solution = Solution()
words = ["Hello","Alaska","Dad","Peace"]
print(solution.findWords(words)) # ["Alaska","Dad"]
words = ["omk"]
print(solution.findWords(words)) # []
words = ["adsdf","sfd"]
print(solution.findWords(words)) # ["adsdf","sfd"]
