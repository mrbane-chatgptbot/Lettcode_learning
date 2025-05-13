class Solution(object):
    def romanToInt(self, s):
        output = 0
        prev_value = 0
        roman_to_int = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        for num in reversed(s):
            cur_val = roman_to_int[num]
            if cur_val < prev_value:
                output -= cur_val
            else:
                output += cur_val
            prev_value = cur_val
        return output
