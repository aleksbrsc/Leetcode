# Leetcode 141: Linked List Cycle
# linked list

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # first guess
    def hasCycle2(self, head):
        nodes = []
        dummy = head

        while dummy:
            if dummy in nodes: return True
            nodes.append(dummy)
            dummy = dummy.next

        return False
    
    # hare and tortoise
    def hasCycle(self, head):
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True
            
        return False

solution = Solution()

head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(-4)
head.next.next.next.next = head.next # pos 2
print(solution.hasCycle(head)) # True

head2 = ListNode(1)
head2.next = ListNode(2)
head2.next.next = head2 # pos 0
print(solution.hasCycle(head2)) # True

head3 = ListNode(1) 
# pos -1 (no cycle)
print(solution.hasCycle(head3)) # False



# || testing

# print(" || NEW LINKED LIST")
# printing = head
# i = 0
# while printing:
#     print(printing.val)
#     printing = printing.next
#     i += 1
#     if i == 20:
#         break