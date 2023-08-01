from typing import List, Optional
import math
from copy import deepcopy


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        list_size = 1
        other_head = head
        while other_head.next:
            other_head = other_head.next
            list_size += 1

        list_head = head
        for _ in range(list_size // 2 - 1):
            list_head = list_head.next

        old_list = list_head.next

        new_list = None
        while old_list:
            new_list, new_list.next, old_list = old_list, new_list, old_list.next

        curr = None
        while prev:
            # curr, prev = ListNode(prev.val, curr), prev.next
            curr, prev.next, prev = prev, curr, prev.next

        prev = None
        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        max_val = 0
        while head_of_reversed:
            max_val = max(max_val, head_of_reversed.val + head.val)
            head_of_reversed = head_of_reversed.next
            head = head.next

        return max_val

