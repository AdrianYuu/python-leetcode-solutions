# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        # first, we need to split the list into two parts
        # by using the slow and fast pointer
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # the start of the second list is next of slow
        second = slow.next
        slow.next = None # detach first from second

        # now reverse the second list
        prev = None
        curr = second

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # the start of the second list is prev

        # merge the two list into one alternately
        # because the second list, it's shorter we use second as condition

        while prev:
            temp1 = head.next
            temp2 = prev.next

            head.next = prev
            prev.next = temp1

            head = temp1
            prev = temp2