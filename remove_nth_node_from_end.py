# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n_from_end: int) -> Optional[ListNode]:
        print("starting process")
        dummy_head = ListNode(0, head)
        slow_pointer = fast_pointer = d

        for i in range(n+1):
            print("current count - ", i)
            fast_pointer = fast_pointer.next
        
        while fast_pointer:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next

        slow_pointer.next = slow_pointer.next.next
        # 0->1->3->4->5
        return dummy_head.next

        
