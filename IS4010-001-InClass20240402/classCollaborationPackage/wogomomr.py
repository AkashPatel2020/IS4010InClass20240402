# Name: Maddy Wogomon
# email: wogomomr@mail.uc.edu
# Assignment Number: In Class 4/2/2024
# Due Date:
# Course/Section: IS4010-002
# Semester/Year: Spring 2024
# Brief Description of the assignment:

# Brief Description of what this module does. Do not copy/paste from a previous assignment. Put some thought into this.
# Citations:
# Anything else that's relevant:
def wogomomr(s: str) -> int:
    # Create a dictionary to map Roman numerals to integers
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    total = 0
    prev_value = 0
    
    # Iterate through the string from right to left
    for char in reversed(s):
        value = roman_values[char]
        
        # If the current value is smaller than the previous value, subtract it
        if value < prev_value:
            total -= value
        else:
            total += value
        
        # Update the previous value
        prev_value = value
    
    return total

# Example usage
if __name__ =="__main__":

    print(wogomomr("III"))      # Output: 3
    print(wogomomr("LVIII"))    # Output: 58
    print(wogomomr("MCMXCIV"))  # Output: 1994
