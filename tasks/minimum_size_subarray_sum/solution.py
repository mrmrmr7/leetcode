from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left_border = 0
        right_border = -1

        min_arr_len = float('inf')
        curr_sum = 0

        while right_border < len(nums)\
                and left_border < len(nums):
            if curr_sum >= target:
                min_arr_len = min(min_arr_len, right_border - left_border + 1)
                curr_sum -= nums[left_border]
                left_border += 1

                if left_border > right_border:
                    right_border += 1
                    curr_sum += nums[right_border]
            elif right_border < len(nums) - 1:
                right_border += 1
                curr_sum += nums[right_border]
            else:
                curr_sum -= nums[left_border]
                left_border += 1

        return min_arr_len if min_arr_len < float('inf') else 0


