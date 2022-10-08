class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window_start, max_length, max_repeat_letter_count = 0, 0, 0
        frequency_map = {}

    
        for window_end in range(len(s)):
            right_char = s[window_end]
            if right_char not in frequency_map:
                frequency_map[right_char] = 0
            frequency_map[right_char] += 1
            max_repeat_letter_count = max(max_repeat_letter_count, frequency_map[right_char])
            if (window_end - window_start + 1 - max_repeat_letter_count) > k:
                left_char = s[window_start]
                frequency_map[left_char] -= 1
                window_start += 1

            max_length = max(max_length, window_end - window_start + 1)
        return max_length
