# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def length(self, head):
        curr = head
        count = 0
        while curr:
            count += 1
            curr = curr.next
        return count

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = self.length(head)
        temp = head
        if n == length:
            head = temp.next
            temp.next = None
        for i in range(length - n - 1):
            temp = temp.next
        if temp.next and temp.next.next:
            temp.next = temp.next.next
        else:
            temp.next = None
        return head