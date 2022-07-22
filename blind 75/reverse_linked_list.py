# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #         if head is None or head.next is None:
        #             return head

        #         current = head
        #         dummy = current
        #         stored = []

        #         # 1 -> 2 -> 3  ==> 3 -> 2 -> 1
        #         while head:
        #             stored.append(head.val)
        #             head = head.next

        #         for i in range(len(stored) - 1, -1, -1):
        #             current.val = stored[i]
        #             current = current.next

        #         return dummy

        prevNode, currNode = None, head
        while currNode:
            nextNode = currNode.next
            currNode.next = prevNode
            prevNode = currNode
            currNode = nextNode
        return prevNode



