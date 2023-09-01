# Leetcode 1290. Convert Binary Number in a Linked List to Integer (easy)
# linked list

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        ans = 0 
        n = len(head)
        i = 1
        dummy_head = ListNode() # dummy node to serve as the head of the linked list
        current = dummy_head # current pointer to keep track of the current node

        for val in head: # Iterate through the elements in the array 'head' and create nodes
            current.next = ListNode(val)
            current = current.next
            ans += 1
        
        linked_list_head = dummy_head.next # 'dummy_head.next' now points to the head of the linked list

        return ans




# test cases
solution = Solution()
head = [1,0,1]
print(solution.getDecimalValue(head)) # 5
"""((101) in base 2 = (5) in base 10)"""
head = [0]
print(solution.getDecimalValue(head)) # 0
