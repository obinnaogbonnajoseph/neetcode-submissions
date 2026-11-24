# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        l, r = list1, list2
        dummy = ListNode(0)
        head = dummy

        while l and r:
            if l.val <= r.val:
                head.next = l
                l = l.next
            else:
                head.next = r
                r = r.next
            head = head.next

        if l:
            head.next = l
        elif r:
            head.next = r

        return dummy.next
