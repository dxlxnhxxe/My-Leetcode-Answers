class Solution:
    def romanToInt(self, s: str) -> int:
        values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        
# A variable to store the result
        result = 0
        
# A loop to iterate through the roman numeral from left to right
        for i in range(len(s)):
        
# If the current symbol is smaller than the next symbol, subtract its value from the result
            if i < len(s) - 1 and values[s[i]] < values[s[i + 1]]:
                result -= values[s[i]]
    
# Otherwise, add its value to the result
            else:
                result += values[s[i]]
 # Return the result
        return result