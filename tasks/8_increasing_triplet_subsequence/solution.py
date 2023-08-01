from typing import  List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first_val = float('inf')
        second_val = float('inf')

        for num in nums:
            if num <= first_val:
                first_val = num
            elif num <= second_val:
                second_val = num
            else:
                return True

        return False
