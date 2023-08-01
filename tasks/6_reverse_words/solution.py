import re

class Solution:
    def reverseWords(self, s: str) -> str:
        # s_arr = re.split(r'\s+', s.strip())
        # r = list(reversed(s_arr))
        return ' '.join(s.split()[::-1])