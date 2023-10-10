class Solution:
    def sum(self, num1: int, num2: int) -> int:
         if -100 <= num1 <= 100 and -100 <= num2 <= 100:
            return num1 + num2
         else:
            return "Input numbers are out of range."