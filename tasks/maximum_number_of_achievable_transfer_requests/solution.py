from typing import List


class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        n_from = [0] * n
        n_to = [0] * n

        for request in requests:
            n_from[request[0]] += 1
            n_to[request[1]] += 1

        res = 0
        for f, t in zip(n_from, n_to):
            res += min(f, t)

        return res

