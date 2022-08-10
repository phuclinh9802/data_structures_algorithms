def reorder_list(head):
    # we can use 2 pointer approach

    # find the middle of the list
    slow, fast = head, head.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # then we reverse the second half
    second = slow.next
    prev = slow.next = None

    while second:
        tmp = second.next
        second.next = prev
        prev = second
        second = tmp

    # then we merge 2 halves
    first, second = head, prev

    while second:
        tmp1, tmp2 = first.next, second.next
        first.next = second
        second.next = tmp1
        first, second = tmp1, tmp2