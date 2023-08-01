from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left_border = right_border = 0

        zeros_count = 0
        latest_zero_detected = -1
        max_window = 0

        while right_border < len(nums):
            if not nums[right_border]:
                left_border = latest_zero_detected + 1
                latest_zero_detected = right_border
                zeros_count += 1

            right_border += 1
            max_window = max(max_window, right_border - left_border)

        return max_window - int(zeros_count > 0)






