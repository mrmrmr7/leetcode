class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        confusion = t_count = f_count = 0
        l_point = r_point = 0

        while r_point < len(answerKey):
            if answerKey[r_point] == 'T':
                t_count += 1
            else:
                f_count += 1

            while t_count > k and f_count > k:
                if answerKey[l_point] == 'T':
                    t_count -= 1
                else:
                    f_count -= 1

                l_point += 1

            confusion = max(confusion, r_point - l_point + 1)
            r_point += 1

        return confusion