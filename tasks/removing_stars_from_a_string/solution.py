from collections import deque

class Solution:
    def removeStars(self, s: str) -> str:
        d = deque()

        for char in s:
            if char == '*':
                d.pop()
            else:
                d.append(char)

        return ''.join(d)
