# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # first, go through brute force
        # current1 node to keep track of l1, current2 node to keep track of l2
        sum = 0
        store1 = store2 = 0
        current1 = l1
        current2 = l2

        i = j = 1
        while l1:
            store1 += l1.val * i
            i *= 10
            l1 = l1.next

        while l2:
            store2 += l2.val * j
            j *= 10
            l2 = l2.next

        stored = None
        if i > j:
            stored = current1
        else:
            stored = current2
        ref = stored

        sum = store1 + store2
        if sum == 0:
            node = ListNode(0)
            return node

        i = int(log10(sum))

        if i == 0 and log10(sum) >= 1:
            i += 1

        while i >= 0:
            if i == 0:
                stored.val = sum
                break
            stored.val = sum % 10
            sum = sum // 10
            i -= 1
            if stored.next is None:
                stored.next = ListNode(sum)
                break
            stored = stored.next

        return ref


