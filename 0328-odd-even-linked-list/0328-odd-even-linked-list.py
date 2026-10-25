# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode | None) -> ListNode | None:
        if head == None:
            return None

        if head.next == None or head.next.next == None:
            return head

        odd = head
        even = head.next
        evenHead = head.next

        while (even != None and even.next != None):
            odd.next = odd.next.next
            even.next = even.next.next
            ## After pointers are changed, only one step to move ahead
            odd = odd.next
            even = even.next
        
        odd.next = evenHead

        return head