# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverse(self, head: ListNode) -> ListNode:
        ## Reversing using recursion
        if head == None or head.next == None:
            return head
        newHead = self.reverse(head.next)
        front = head.next
        front.next = head
        head.next = None
        return newHead

    def isPalindrome(self, head: ListNode | None) -> bool:
        slow = head
        fast = head
        ## Step 1
        ## fast.next for standing on the middle node (odd)
        ## fast.next.next to stay one node before the two equal nodes (even)
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next

        ## Step 2
        ## reverse the second half
        newHead = self.reverse(slow.next)
        first = head
        second = newHead

        ## Step 3 check palindrome
        while second != None:
            if first.val != second.val:
                self.reverse(newHead)
                return False
            
            first = first.next
            second = second.next
        
        self.reverse(newHead)
        return True