class Solution:
    def _is_string_dividable(self, source, part):
        part_len = len(part)
        source_len = len(source)
        is_str_divided = True
        for i in range(0, source_len, part_len):
            is_str_divided = source[i:i + part_len] == part
            if not is_str_divided:
                break
        return is_str_divided

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len_str1 = len(str1)
        len_str2 = len(str2)

        short_str = str1 if len_str1 < len_str2 else str2
        long_str = str1 if len_str1 >= len_str2 else str2

        min_len = min(len_str1, len_str2)

        gcd = ''
        for chunk_len in range(min_len, 0, -1):
            if len_str2 % chunk_len or len_str1 % chunk_len:
                continue

            chunk = short_str[:chunk_len]

            if not self._is_string_dividable(short_str, chunk):
                continue

            if not self._is_string_dividable(long_str, chunk):
                continue

            gcd = chunk
            break

        return gcd
