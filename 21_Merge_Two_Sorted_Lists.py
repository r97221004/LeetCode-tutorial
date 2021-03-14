"""
Merge two sorted linked lists and return it as a sorted list. The list should 
be made by splicing together the nodes of the first two lists.
"""

# 方法一

"""
不常操作鏈表結構， 要記得多看!!!!!
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        curr = dummy
        while l1 != None and l2 != None:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr =curr.next
        if l1 != None:
            curr.next = l1
        if l2 != None:
            curr.next = l2
        return dummy.next

# 方法二

"""
使用遞迴的方式來處理，更容易理解。
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
#         def FindMin(n1, n2):
#             if n1 == None:
#                 return n2
#             if n2 == None:
#                 return n1
#             if n1.val < n2.val:
#                 n1.next = FindMin(n1.next, n2)
#                 return n1
#             else:
#                 n2.next = FindMin(n2.next, n1)
#                 return n2
#         return FindMin(l1, l2)
        

            
        
                






