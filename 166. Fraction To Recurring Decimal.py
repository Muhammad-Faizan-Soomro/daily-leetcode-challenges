# Problem: 166. Fraction to Recurring Decimal
# Task:
# - Convert a fraction (numerator / denominator) into its decimal representation as a string.
# - If the decimal part is repeating, enclose the repeating portion in parentheses.
#
# Example:
#   numerator = 1, denominator = 2
#   → "0.5"
#
#   numerator = 2, denominator = 1
#   → "2"
#
#   numerator = 2, denominator = 3
#   → "0.(6)"   (since 0.666... repeats)
#
#   numerator = 4, denominator = 333
#   → "0.(012)" (since 0.012012... repeats)
#
# Approach:
# 1. Handle sign: if result is negative, add "-".
# 2. Compute the integer part (numerator // denominator).
# 3. If no remainder, return integer part as result.
# 4. Otherwise, start building the fractional part:
#       - Multiply remainder by 10, divide by denominator to get next digit.
#       - Store each remainder in a map to track positions in the result string.
#       - If a remainder repeats → we found the recurring cycle, insert parentheses.
# 5. Return the constructed result string.
#
# Time Complexity: O(n)
#   - At most, each unique remainder appears once (before repetition).
#   - In the worst case, the cycle length ≤ denominator.
#
# Space Complexity: O(n)
#   - Hashmap `seen` stores remainders and their positions.
#
# Note: This is the classic "detect repeating remainders" technique, 
#       similar to detecting cycles in long division.
#
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        # Case 1: numerator = 0 → result is "0"
        if numerator == 0:
            return "0"
        
        result = ''  
        
        # Case 2: Handle negative sign
        if numerator * denominator < 0:
            result += "-"

        # Work with absolute values
        numerator = abs(numerator)
        denominator = abs(denominator)

        # Step 1: Add integer part
        result += str(numerator // denominator)

        # Step 2: Compute initial remainder
        remainder = numerator % denominator

        # If no remainder → exact division, return result
        if remainder == 0:
            return result

        # Step 3: Prepare for fractional part
        result += "."    
        seen = {}  # remainder → position in result string

        # Step 4: Long division simulation
        while remainder != 0:
            # If this remainder was seen before → cycle detected
            if remainder in seen:
                position = seen[remainder]
                # Insert "(" at cycle start and ")" at end
                result = result[:position] + "(" + result[position:] + ")"
                break
            
            # Mark position where this remainder first appeared
            seen[remainder] = len(result)

            # Long division: multiply remainder by 10
            remainder *= 10
            
            # Next digit in fractional part
            digit = remainder // denominator
            result += str(digit)

            # Update remainder
            remainder = remainder % denominator
            
        return result
