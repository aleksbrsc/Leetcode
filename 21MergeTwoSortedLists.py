# Leetcoded 20: Merge Two Sorted Lists
# Linked List

# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        sentinel_head = ListNode(-1)
        tail = sentinel_head

        while True:
            if list1 is None:
                tail.next = list2
                break
            elif list2 is None:
                tail.next = list1
                break
            if list1.val <= list2.val:
                new_node = list1
                list1 = list1.next
                new_node.next = tail.next
                tail.next = new_node
            else: 
                new_node = list2
                list2 = list2.next
                new_node.next = tail.next
                tail.next = new_node
            tail = tail.next

        # printing = sentinel_head.next
        # while printing:
        #     print(printing.val)
        #     printing = printing.next

        return sentinel_head.next

solution = Solution()
first = ListNode(1)
first.next = ListNode(2)
first.next.next = ListNode(4)
second = ListNode(1)
second.next = ListNode(3)
second.next.next = ListNode(4)
print(solution.mergeTwoLists(first, second))