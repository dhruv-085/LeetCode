# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

            ## Step 1
            # For checking if loop exists
            if fast == slow:
                slow = head
                
                ## Step 2 (move by one distance)
                # Finding the loop starting node 
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                
                return slow
        return None
            