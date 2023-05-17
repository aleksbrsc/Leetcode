# Leetcode 49: Group Anagrams
from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagram_map = defaultdict(list)
        result = []

        for word in strs:
            sorted_word = tuple(sorted(word))
            anagram_map[sorted_word].append(word)
        
        for value in anagram_map.values():
            result.append(value)
        
        return result
    
# test cases    
solution = Solution()
print(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(solution.groupAnagrams(["wow", "woo", "rat", "tar", "art", "owo"]))