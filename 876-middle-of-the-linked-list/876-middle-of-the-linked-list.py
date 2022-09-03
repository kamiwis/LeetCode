# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        fast = head
        slow = head
        while fast:
            fast = fast.next
            if count % 2 == 0 and fast is not None:
                slow = slow.next
            count += 1
        return slow
            