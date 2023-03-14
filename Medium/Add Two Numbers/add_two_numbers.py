# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_string = str(l1.val)
        l2_string = str(l2.val)
        l1_current = l1.next
        l2_current = l2.next
        while l1_current != None:
            l1_string = str(l1_current.val) + l1_string
            l1_current = l1_current.next
        while l2_current != None:
            l2_string = str(l2_current.val) + l2_string
            l2_current = l2_current.next
        result_str = str(int(l1_string)+int(l2_string))[::-1]
        print(result_str)
        if len(result_str) == 1:
            return ListNode(int(result_str[0]))
        sol_list_node = ListNode(int(result_str[0]), ListNode())
        current_node = sol_list_node.next
        for i in range(1, len(result_str)):
            current_node.val = int(result_str[i])
            if i == len(result_str)-1:
                current_node.next = None
                break
            current_node.next = ListNode()
            current_node = current_node.next
        return sol_list_node
