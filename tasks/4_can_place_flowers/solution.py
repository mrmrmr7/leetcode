from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        available_places = 0
        if len(flowerbed) == 1:
            available_places += 1 if flowerbed[0] == 0 else 0
        elif len(flowerbed) == 2:
            available_places += 1 if flowerbed[0] == 0 and flowerbed[1] == 0 else 0
        else:
            if 0 == flowerbed[0] == flowerbed[1]:
                available_places += 1
                flowerbed[0] = 1

            for i in range(1, len(flowerbed) - 1):
                if 0 == flowerbed[i] == flowerbed[i-1] == flowerbed[i+1]:
                    flowerbed[i] = 1
                    available_places += 1

            if 0 == flowerbed[-1] == flowerbed[-2]:
                available_places += 1
                flowerbed[-1] = 1

        return available_places >= n




