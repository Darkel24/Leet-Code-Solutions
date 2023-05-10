# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,root) :
        if root is None or root.next is None :
            return root
        prev,cur,fut = None,root,root.next
        
        while cur.next :
            cur.next = prev
            prev = cur
            cur = fut
            fut = cur.next
        cur.next = prev

        head,end = cur,None
        while cur :
            end = cur
            cur = cur.next
        return head,end


    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if k == 0 or head is None or head.next is None:
            return head

        linked_length = 0
        cur = head

        while cur :
            linked_length += 1
            cur = cur.next
        
        k = k % linked_length
        if k == 0 :
            return head
            
        temp_head,end = self.reverse(head)
        breakpt = temp_head
        
        while k > 1 :
            k -= 1
            breakpt = breakpt.next
        
        
        cur,end = self.reverse(temp_head)
        
        while cur :
            if cur.next == breakpt :
                cur.next = None
                end.next = head
                return breakpt
            cur = cur.next
        
