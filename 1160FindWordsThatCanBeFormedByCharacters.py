# Leetcode 1160. Find Words That Can Be Formed by Characters (easy)
# string, array

class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        ans = 0
        letters = []

        for c in sorted(chars):
            letters.append(c)

        for word in words:
                new = ""
                i = 0
                usable = letters[:] 
                while i < len(word):
                    if word[i] in usable:
                        usable.remove(word[i])
                        new += word[i]
                    if new == word:
                          ans += len(word)
                    i += 1

        return ans

# test cases
solution = Solution()
words = ["cat","bt","hat","tree"]
chars = "atach"
print(solution.countCharacters(words, chars)) # 6
words = ["hello","world","leetcode"]
chars = "welldonehoneyr"
print(solution.countCharacters(words, chars)) # 10