from typing import List
from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        vote_q = deque(list(senate))

        d_count = 0
        r_count = 0

        while (v_len := len(vote_q)) > 1 \
                and v_len != d_count \
                and v_len != r_count:
            vote = vote_q.popleft()
            if vote == 'D':
                if r_count:
                    r_count -= 1
                else:
                    d_count += 1
                    vote_q.append(vote)
            else:
                if d_count:
                    d_count -= 1
                else:
                    r_count += 1
                    vote_q.append(vote)

        if len(vote_q) == d_count:
            return 'Dire'

        if len(vote_q) == r_count:
            return 'Radiant'

        return 'Radiant' if vote_q.pop() == 'R' else 'Dire'
