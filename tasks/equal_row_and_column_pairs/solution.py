from typing import List

from collections import Counter

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        rows_counters = [dict(Counter(grid[i])) for i in range(n)]
        cols_counters = []

        for i in range(n):
            cols_counters.append(dict(Counter([grid[j][i] for j in range(n)])))

        matches_count = 0
        for i, row_counter in enumerate(rows_counters):
            for j, col_counter in enumerate(cols_counters):
                if row_counter == col_counter:
                    for k in range(n):
                        if not grid[i][k] == grid[k][j]:
                            break
                    else:
                        matches_count += 1

        return matches_count



        print()

