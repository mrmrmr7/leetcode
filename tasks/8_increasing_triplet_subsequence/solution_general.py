from typing import  List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        longest_sequence = [nums[0]]

        for num in nums[1:]:
            for i, e in enumerate(longest_sequence):
                if num <= e:
                    longest_sequence[i] = num
                    break
            else:
                longest_sequence.append(num)

            if len(longest_sequence) >= 3:
                return True

        return False
