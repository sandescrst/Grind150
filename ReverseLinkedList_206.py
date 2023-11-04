class ListNode:
    def __init__(self, val=0, next= None):
        self.val = val
        self.next = next

class Solution:


    def reverse(self, head,):
        prev = None
        curr = head
        
        while curr:
            
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev
    
