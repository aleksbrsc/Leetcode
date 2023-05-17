# Leetcode 242: Valid Anagram (easy)
# arrays, hashmaps or sort
def extract_characters(string):
    extracted_chars = []
    for i in string:
        extracted_chars.append(i)
    return extracted_chars

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        anagram_chars = [] # list of characters to be used in anagram extracted from s string, removed each time a char is found in extracted_chars_t
        t_remaining = [] # list of characters in t string, removed each time a char is found in the list of anagram chars
        # list of extracted characters for both strings
        extracted_chars_s = extract_characters(s)
        extracted_chars_t = extract_characters(t)

        for char in extracted_chars_s:
            anagram_chars.append(char) # populating the list of characters for the anagram
        
        for char in extracted_chars_t:
            t_remaining.append(char) # populating the list of characters remaining in t string
        
        for char in extracted_chars_t:
            if char in anagram_chars:
                anagram_chars.remove(char) # remove from list of anagram characters
                t_remaining.remove(char) # remove from list of t characters remaining

        # returns True if the list of anagram chars is empty (all used) and the list of t string chars remaining is not empty (all used, no left over chars)
        return not anagram_chars and not t_remaining
    
    # one line solution I thought of when I heard of sort, beats my previous time and space complexity
    def isAnagramSort(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t) # returns true if both sorted strings are the same

# test cases
solution = Solution()
print(solution.isAnagram("anagram", "nagaram"))
print(solution.isAnagram("anagram", "nagaramm"))
print(solution.isAnagramSort("anagram", "nagaram"))
print(solution.isAnagramSort("anagram", "nagaramm"))