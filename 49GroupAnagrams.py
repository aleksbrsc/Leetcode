# Leetcode 49: Group Anagrams (medium)
# stack

from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # defaultdict never raises a KeyError as it provides a default value for the key that does not exist
        # this is useful when we are storing collections inside hashmaps, default hashmap needs them to be initialized 
        # but in defaultdict they are already initialized by default, which is convenient
        anagram_map = defaultdict(list)
        result = []

        for word in strs:
            # sorting the words lexicographically, the sorted word will become a key in the hashmap
            # sorted makes a list which is a mutable datatype so youll get a key error, hence casting to immutable tuple
            sorted_word = tuple(sorted(word))
            # appending each word as a value to its key which is the sorted version
            anagram_map[sorted_word].append(word) 

        # we can't just return the anagram hashmap with its sorted keys, we need to append each value to the list instead.
        for value in anagram_map.values():
            result.append(value)
        
        return result
    
# test cases    
solution = Solution()
print(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(solution.groupAnagrams(["wow", "woo", "rat", "tar", "art", "owo"]))