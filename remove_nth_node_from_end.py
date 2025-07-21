from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create a dummy node to handle cases where the head needs to be removed
        dummy_node = ListNode(0, head)
        pre_target = scout_pointer = dummy_node

        for _ in range(n+1):
            scout_pointer = scout_pointer.next
        
        while scout_pointer:
            pre_target = pre_target.next
            scout_pointer = scout_pointer.next

        pre_target.next = pre_target.next.next

        return dummy_node.next