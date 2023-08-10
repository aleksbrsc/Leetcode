# Leetcode 500. Keyboard Row (easy)
# array, string

class Solution(object):
    def findWords(self, words):
        ans = []
        q = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
        a = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
        z = ['z', 'x', 'c', 'v', 'b', 'n', 'm']

        for word in words:
            lower_word = word.lower()
            broken = False
            belonging = q
            if lower_word[0] in a: belonging = a
            if lower_word[0] in z: belonging = z
            for letter in lower_word:
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
