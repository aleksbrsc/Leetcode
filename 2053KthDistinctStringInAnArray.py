# Leetcode 2053. Kth Distinct String in an Array (easy)
# array, string

class Solution(object):
    def kthDistinct2(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        string_frequencies = {}
        distincts = []

        for string in arr:
            if string not in string_frequencies:
                string_frequencies[string] = 1
            else:
                string_frequencies[string] += 1

        for string in string_frequencies:
            if string_frequencies[string] == 1:
                distincts.append(string)
        
        if len(distincts) < k:
            return ""
        
        return distincts[k-1]
    
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        string_frequencies = {}

        for string in arr:
            if string not in string_frequencies:
                string_frequencies[string] = 1
            else:
                string_frequencies[string] += 1

        count = 0
        for string in arr:
            if string_frequencies[string] == 1: 
                count += 1
                if count == k: return string

        return ""

# test cases
solution = Solution()
arr = ["d","b","c","b","c","a"]
k = 2
print(solution.kthDistinct(arr, k)) # "a"
arr = ["aaa","aa","a"]
k = 1
print(solution.kthDistinct(arr, k)) # "aaa"
arr = ["a","b","a"]
k = 3
print(solution.kthDistinct(arr, k)) # ""