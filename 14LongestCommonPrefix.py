# Leetcode 14: Longest Common Prefix (easy)

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        shortest_word_length = len(min(strs, key=len)) # range is always the length of shortest word 
        current = [] # list for holding the characters of the current index in the range
        prefix = "" # the longest common prefix initially

        for index in range(shortest_word_length): # iterates through range of the length of shortest word
            current = []
            for word in strs: # iterates through the words in the list
                current.append(word[index]) # add char to the current list
                if len(current) == len(strs) and all(letter == current[0] for letter in current): # if list is full with same char
                    prefix += current[0] # adds the common char to prefix string
                    current = [] # resets the current list
            if len(current) == len(strs): # if list is full but not every char is the same
                return prefix # common prefix ends and is returned
        return prefix
    
    # faster solution which sorts the strings, only comparing first string to last string meaning better time complexity () O(n)
    def longestCommonPrefixFaster(self, strs: list[str]) -> str:
        prefix = ""
        # sort the strings lexicographically
        # because if there are any differences in the chars of string, the fastest way to spot them would be comparing only the first and last strings if they are sorted, and not iterating through every character of every word
        strs = sorted(strs) 
        first = strs[0] # first string in the list
        last = strs[-1] # last string in the list
        for i in range(min(len(first), len(last))): # iterates through the characters of the first and last strings
            if first[i] != last[i]:
                return prefix
            prefix += first[i]
        return prefix

# test cases
test = ["flow","flower","flight"] 
test2 = ["dog", "racecar", "car"]
test3 = ["car", "cir"]
solution = Solution()
print(solution.longestCommonPrefix(test))
print(solution.longestCommonPrefix(test2))
print(solution.longestCommonPrefix(test3))
print(solution.longestCommonPrefixFaster(test))
print(solution.longestCommonPrefixFaster(test2))
print(solution.longestCommonPrefixFaster(test3))