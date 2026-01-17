# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        result = dummy

        carry = False

        while l1 or l2 or carry:
            total = 0

            if l1:
                total += l1.val
                l1 = l1.next

            if l2:
                total += l2.val
                l2 = l2.next

            if carry == True:
                total += 1
                carry = False

            # 4 + 6 = 10 % 10 = 0
            # 6 + 6 = 12 % 10 = 2
            if total > 9:
                total -= 10
                carry = True

            dummy.next = ListNode(total, None)
            dummy = dummy.next

        return result.next