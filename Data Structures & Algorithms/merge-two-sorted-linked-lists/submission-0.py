# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        combinedList = ListNode(0)
        curr = combinedList
        l1 = list1
        l2 = list2

        while l1 and l2:
            if l1.val <= l2.val:
                node = ListNode(l1.val)
                curr.next = node
                curr = curr.next
                l1 = l1.next
            else:
                node = ListNode(l2.val)
                curr.next = node
                curr = curr.next
                l2 = l2.next
        curr.next = l1 if l1 else l2 # When one of the lists runs out of nodes, fill the rest of combinedList

        return combinedList.next # The "head" is a dummy head, as combinedList was set to 0. .next is the true head
            