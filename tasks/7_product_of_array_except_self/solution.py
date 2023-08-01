from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ltr = 1

        results = []
        for i in nums:
            ltr *= i
            results.append(ltr)

        rtl = 1
        for i in range(len(nums) - 1, -1, -1):
            if i:
                results[i] = results[i - 1] * rtl
                rtl *= nums[i]
            else:
                results[i] = rtl

        return results
