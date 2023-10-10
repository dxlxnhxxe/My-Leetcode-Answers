# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy_node = ListNode(0)
        head = dummy_node
        p1 = l1
        p2 = l2
        carry = 0

        while p1 or p2:
            val1 = p1.val if p1 else 0
            val2 = p2.val if p2 else 0
            sum = val1 + val2 + carry
            new_val = sum % 10
            new_carry = sum//10
            head.next = ListNode(new_val)
            head = head.next
            carry = new_carry
            
            if p1:
                p1 = p1.next
            if p2:
                p2 = p2.next

        if carry != 0:
            head.next = ListNode(carry)

        return dummy_node.next