"""
Given the head of a sorted linked list, delete all duplicates such that each element 
appears only once. Return the linked list sorted as well.
"""

方法一

"""
linked list 的操作一
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        current = head
        while current:
            runner = current.next
            while runner and current.val == runner.val:
                runner = runner.next
            current.next = runner
            current = runner
        return head


# 方法二

"""
linked list 的操作二
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# class Solution:
#     def deleteDuplicates(self, head: ListNode) -> ListNode:
#         if not head: return None
#         else:
#             dummy = curr = ListNode(-inf)
#             while head:
#                 if curr.val != head.val:
#                     curr.next = head
#                     head = head.next
#                     curr = curr.next
#                     curr.next = None
#                 else:
#                     head = head.next
#             return dummy.next

