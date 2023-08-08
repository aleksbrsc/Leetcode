# Leetcode 2788. Split Strings by Separator (easy)
# array, string

class Solution(object):
    def splitWordsBySeparator(self, words, separator):
        """
        :type words: List[str]
        :type separator: str
        :rtype: List[str]
        """
        ans = []
        refined = []

        for string in words:
            temp = []
            temp.append(string.split(separator))
            for new in temp:
                for s in new:
                    ans.append(s)

        for string in ans:
            if string == "": continue
            refined.append(string)
            

        return refined


        

# test cases
solution = Solution()
words = ["one.two.three","four.five","six"]
separator = "."
print(solution.splitWordsBySeparator(words, separator)) # ["one","two","three","four","five","six"]
words = ["$easy$","$problem$"]
separator = "$"
print(solution.splitWordsBySeparator(words, separator)) # ["easy","problem"]
words = ["|||"]
separator = "|"
print(solution.splitWordsBySeparator(words, separator)) # []