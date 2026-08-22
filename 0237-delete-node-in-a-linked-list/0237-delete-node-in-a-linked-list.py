# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        
        ## we are already given the node which we have to delete, so just overwrite the value of the next node over here and move the pointer to next.next simple right

        node.val = node.next.val
        node.next = node.next.next
        