# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        a=b=head
        c=d=ListNode()
        z=None
        while head and head.next:
            x=head.next
            head.next=z
            z=head
            head=x
            y=head.next
            head.next=z
            z=head
            head=y
            c.next=z
            c=c.next.next
            z=None
        if head:
            c.next=head
        return d.next
