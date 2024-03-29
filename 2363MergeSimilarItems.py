# 2363. Merge Similar Items (easy)
# 2d array, hashmap

from collections import defaultdict
class Solution(object):
    def mergeSimilarItems(self, items1, items2):
        """
        :type items1: List[List[int]]
        :type items2: List[List[int]]
        :rtype: List[List[int]]
        """
        value_to_weights = defaultdict(int)

        for item in items1:
            value_to_weights[item[0]] += item[1]
        for item in items2:
            value_to_weights[item[0]] += item[1]
        
        return sorted(value_to_weights.items())

# test cases
solution = Solution()
items1 = [[1,1],[4,5],[3,8]]
items2 = [[3,1],[1,5]]
print(solution.mergeSimilarItems(items1, items2)) # [[1,6],[3,9],[4,5]]
items1 = [[1,1],[3,2],[2,3]]
items2 = [[2,1],[3,2],[1,3]]
print(solution.mergeSimilarItems(items1, items2)) # [[1,4],[2,4],[3,4]]
items1 = [[1,3],[2,2]]
items2 = [[7,1],[2,2],[1,4]]
print(solution.mergeSimilarItems(items1, items2)) # [[1,7],[2,4],[7,1]]