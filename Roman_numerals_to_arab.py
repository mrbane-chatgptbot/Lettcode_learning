class Solution(object):
    def romanToInt(self, s):
        output = 0
        prev_value = 0
        for num in reversed(s):
            match num:
                case "I":
                    cur_val = 1
                case "V":
                    cur_val = 5
                case "X":
                    cur_val = 10
                case "L":
                    cur_val = 50
                case "C":
                    cur_val = 100
                case "D":
                    cur_val = 500
                case "M":
                    cur_val = 1000
            if output < prev_value:
                output -= cur_val
            else:
                output += cur_val
            prev_value = cur_val
