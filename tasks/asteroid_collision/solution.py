from typing import List
from collections import deque


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        left_asteroids = deque(asteroids[:1])

        for next_asteroid in asteroids[1:]:
            while len(left_asteroids) > 0:
                prev_asteroid = left_asteroids[-1]
                if next_asteroid < 0 < prev_asteroid:
                    if abs(next_asteroid) > abs(prev_asteroid):
                        left_asteroids.pop()
                        continue
                    elif abs(next_asteroid) == abs(prev_asteroid):
                        left_asteroids.pop()
                    break

                left_asteroids.append(next_asteroid)
                break
            else:
                left_asteroids.append(next_asteroid)

        return list(left_asteroids)
