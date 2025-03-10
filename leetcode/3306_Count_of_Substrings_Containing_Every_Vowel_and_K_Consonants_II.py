class Solution:

    def countOfSubstrings(self, word: str, k: int) -> int:
        letter_dict = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
        hard_stop_dict = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
        i = j = 0
        res = 0
        res_sum = k * 10 + 5
        cur_sum = 0
        hard_stop = 0
        while j < len(word):
            letter = word[j]
            if letter in letter_dict:
                if hard_stop != 0:
                    hard_stop_dict[letter] += 1
                else:
                    if letter_dict[letter] == 0:
                        cur_sum += 1
                    letter_dict[letter] += 1
                j += 1
            else:
                cur_sum += 10
                if cur_sum == res_sum:
                    res += 1
                    hard_stop = j
                    j += 1
                elif cur_sum > res_sum:
                    j = hard_stop
                    cur_sum = res_sum
                    while i < j:
                        first_letter = word[i]
                        letter_dict[first_letter] -= 1
                        if letter_dict[first_letter] == 0:
                            cur_sum -= 1
