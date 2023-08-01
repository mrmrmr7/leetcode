from typing import List, Optional
import math


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tail = head

        q_size = 1
        while tail.next:
            tail = tail.next
            q_size += 1

        head_storage = head

        for _ in range(q_size // 2):
            tail.next = head.next
            tail = tail.next

            head.next = head.next.next
            head = head.next

        tail.next = None

        return head_storage
