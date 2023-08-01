from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeros_positions = []
        max_window_len = 0
        left_window_border = 0

        for i, v in enumerate(nums):
            if not v:
                zeros_positions.append(i)
                if len(zeros_positions) > k:
                    left_window_border = zeros_positions.pop(0) + 1

            max_window_len = max(i - left_window_border + 1, max_window_len)

        return max_window_len
