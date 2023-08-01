from typing import List
from queue import Q


class Solution:
    def decodeString(self, s: str) -> str:
        segments = ['']
        num = 0

        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            elif char == '[':
                segments.append(num)
                segments.append('')
                num = 0
            elif char == ']':
                part = segments.pop()
                mult = segments.pop()

                segments.append(segments.pop() + part * mult)
            else:
                segments[-1] += char

        return ''.join(segments)
