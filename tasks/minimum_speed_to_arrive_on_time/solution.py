from typing import List
from math import ceil

class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        min_speed = 1
        max_speed = 10**7
        curr_speed = (min_speed + max_speed) // 2

        is_acc_limit_reached = False
        while not is_acc_limit_reached:
            t = sum([ceil(e / curr_speed) for e in dist[:-1]])
            t += dist[-1] / curr_speed

            if t > hour:
                max_speed = curr_speed
                curr_speed = (min_speed + curr_speed) / 2
            else:
                t = sum([ceil(e / curr_speed + 1) for e in dist[:-1]])
                t += dist[-1] / curr_speed + 1

                is_acc_limit_reached = True

        return curr_speed


