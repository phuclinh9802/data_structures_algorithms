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
        # get l1 number
        while l1:
            store1 += l1.val * i
            i *= 10
            l1 = l1.next

        # get l2 number
        while l2:
            store2 += l2.val * j
            j *= 10
            l2 = l2.next

        stored = None
        # store linked list with larger length
        if i > j:
            stored = current1
        else:
            stored = current2
        ref = stored

        # get sum between 2 numbers
        sum = store1 + store2

        # check if sum = 0 -> return new node of 0
        if sum == 0:
            node = ListNode(0)
            return node

        # get number of digits of sum
        i = int(log10(sum))

        # check if sum > 0 and < 10
        if i == 0 and log10(sum) >= 1:
            i += 1 # i should be 1 for base case

        # loop through digits of sum
        while i >= 0:
            # if digits in sum = length of stored linked list
            if i == 0:
                stored.val = sum
                break
            stored.val = sum % 10
            sum = sum // 10
            i -= 1
            # if # of digits in sum > length of stored linked list
            if stored.next is None:
                stored.next = ListNode(sum)
                break
            stored = stored.next

        return ref


