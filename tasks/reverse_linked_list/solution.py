from typing import List, Optional
import math


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode], previous: Optional[ListNode] = None) -> Optional[ListNode]:
        if not head:
            return head

        if not head.next:
            return head

        reversed_list = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return reversed_list
