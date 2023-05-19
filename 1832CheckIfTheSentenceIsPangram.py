# Leetcode 1832: Check if the Sentence Is Pangram (easy)
# string


class Solution(object):
    # my basic solution
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        l = ""

        for char in sentence:
            if char not in l and char == char.lower():
                l += char

        return len(l) == 26

    # smart one line solution, casting string to a set means storing only the unique elements of a string,
    # since the constraint is that the string is made of lowercase alphabets: then you can just return True if length of the set is 26
    def checkIfPangramOneLine(self, sentence):
        return len(set(sentence)) == 26

# test cases
solution = Solution()
sentence = "thequickbrownfoxjumpsoverthelazydog"
print(solution.checkIfPangram(sentence))
print(solution.checkIfPangramOneLine(sentence))