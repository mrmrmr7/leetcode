from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        right_sum = sum(nums[1:])
        left_sum = 0

        for i in range(len(nums) - 1):
            if right_sum == left_sum:
                return i
            else:
                left_sum += nums[i]
                right_sum -= nums[i + 1]

                set().difference()

        [].__eq__()

        return -1 if left_sum else len(nums) - 1
