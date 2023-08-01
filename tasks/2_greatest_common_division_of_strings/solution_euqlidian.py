class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len_str1, len_str2 = len(str1), len(str2)
        if len_str2 > len_str1:
            return self.gcdOfStrings(str2, str1)
        elif not str2:
            return str1
        elif str1[:len_str2] == str2:
            return self.gcdOfStrings(str1[len_str2:], str2)
        return ''
