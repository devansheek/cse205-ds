# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode()
        tail = dummyHead
        carry = 0
        while l1 or l2 or carry != 0:
            if l1:
                digit1 = l1.val
            else:
                digit1 = 0
            if l2:
                digit2 = l2.val
            else:
                digit2 = 0

            addition = digit1 + digit2 + carry
            ones_place = addition % 10
            carry = addition // 10
            new_node = ListNode(ones_place)
            tail.next = new_node
            tail = new_node
            
            if l1:
                l1 = l1.next
            else:
                l1 = None
            if l2:
                l2 = l2.next
            else:
                l2 = None
        return dummyHead.next