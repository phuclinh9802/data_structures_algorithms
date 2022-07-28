# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = None
        current = head
        stored = head
        count = 0

        while stored:
            count += 1
            stored = stored.next

        if count == 1 and n == 1:
            return None

        if count == n:
            head = head.next
            return head

        nth = count - n
        i = 0
        while i < nth:
            prev = current
            current = current.next

            i += 1

        prev.next = current.next
        return head

