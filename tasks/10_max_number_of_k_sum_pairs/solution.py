from typing import List

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()

        c = 0
        left_pointer = 0
        right_pointer = len(nums) - 1
        while right_pointer > left_pointer:
            if nums[right_pointer] + nums[left_pointer] > k:
                right_pointer -= 1
            elif nums[right_pointer] + nums[left_pointer] == k:
                c += 1
                left_pointer += 1
                right_pointer -= 1
            else:
                left_pointer += 1

        return c
