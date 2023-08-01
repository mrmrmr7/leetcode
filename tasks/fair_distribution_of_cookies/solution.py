from typing import List, Optional
import math


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        ans = float('inf')
        fair = [0] * k

        def backtrack(i):
            nonlocal ans, fair

            if i == len(cookies):
                ans = min(ans, max(fair))
                return

            elif ans <= max(fair):
                return

            for j in range(k):
                fair[j] += cookies[i]
                backtrack(i + 1)
                fair[j] -= cookies[i]

        backtrack(0)
        return ans

# [
#   [0,0], 1
#   [0,0], 2
#   [0,1],
#   [0,1],
#   [1,1], 3
#   [1,1], 4
#   [2,0],
#   [2,2], 5
#   [2,1],
# ]
