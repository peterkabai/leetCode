# https://leetcode.com/problems/multiply-strings/submissions/
class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        # creates a new conversion function to convert from string to int
        def convert(self, num: str) -> int:
            output, digit = 0, 0
            for n in num[::-1]: # loops through in reverse
                v = None
                # converts each digit from a string to an int without using built in functions 
                match n:
                    case "0": v = 0
                    case "1": v = 1
                    case "2": v = 2
                    case "3": v = 3
                    case "4": v = 4
                    case "5": v = 5
                    case "6": v = 6
                    case "7": v = 7
                    case "8": v = 8
                    case "9": v = 9
                # multiplies the value to the correct place, tens, hundreds etc.
                output += (v * 10**digit)
                digit += 1
            return(output)

        return str(convert(self, num1) * convert(self, num2))