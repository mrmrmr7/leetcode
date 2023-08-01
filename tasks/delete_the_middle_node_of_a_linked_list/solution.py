from typing import List, Optional
import math


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        list_size = 1
        second_head = head
        while second_head.next:
            second_head = second_head.next
            list_size += 1

        second_head = head
        for _ in range(list_size // 2 - 1):
            second_head = second_head.next

        if second_head.next and second_head.next.next:
            second_head.next = second_head.next.next
        elif second_head.next:
            second_head.next = None
        else:
            head = None

        return head

