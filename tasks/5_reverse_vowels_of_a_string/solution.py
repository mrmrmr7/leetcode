class Solution:
    def reverseVowels(self, s: str) -> str:
        s_arr = list(s)

        vowels = 'aeiouAEIOU'
        v_positions = [i for i, v in enumerate(s) if v in vowels]

        half_len = len(v_positions) // 2
        v_positions_from = v_positions[:half_len]
        v_positions_to = list(reversed(v_positions[half_len:]))

        for swap_from, swap_to in zip(v_positions_from, v_positions_to):
            s_arr[swap_to], s_arr[swap_from] = s_arr[swap_from], s_arr[swap_to]


        return ''.join(s_arr)