# Leetcode 1299. Replace Elements with Greatest Element on Right Side (easy)
# array

class Solution(object):
    # time limit exceeded
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        ans = []

        for i, n in enumerate(arr):
            highest = 0
            for j in range(i + 1, len(arr)):
                if arr[j] > highest: highest = arr[j]
            if i == len(arr) - 1: continue
            ans.append(highest)

        ans.append(-1)
        return ans
            
    # faster
    def replaceElements(self, arr):
        max = arr[len(arr) - 1]

        for i in range(len(arr)-1, -1, -1):
            if i == len(arr) - 1:
                arr[i] = -1
            else:
                temp = arr[i]
                arr[i] = max
                if max < temp:
                    max = temp

        return arr

# test cases
solution = Solution()
arr = [17,18,5,4,6,1]
print(solution.replaceElements(arr)) # true
arr = [400]
print(solution.replaceElements(arr)) # false