# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head: Optional[ListNode]):
        prev_node = None
        present_node = head
        while present_node:
            next_node = present_node.next
            present_node.next = prev_node
            prev_node = present_node
            present_node = next_node
        return prev_node

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid_node_reversed = self.reverse(slow)
        current = head
        forward = mid_node_reversed
        while forward and current:
            if current.val != forward.val:
                return False
            current = current.next
            forward = forward.next
        return True