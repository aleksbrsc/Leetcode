# Leetcode 1720. Decode XORed Array (easy)
# array

class Solution(object):
    def decode(self, encoded, first):
        """
        :type encoded: List[int]
        :type first: int
        :rtype: List[int]
        """
        arr = [first]

        for i, n in enumerate(encoded):
            arr.append(arr[i] ^ n)

        return arr

# test cases
solution = Solution()
encoded = [1,2,3]
first = 1
print(solution.decode(encoded, first))