#stapleet.py
# Name: Elizabeth Stapleton
# email: stapleet@mai.uc.edu
# Assignment Number: InClass20240402
# Due Date:04-02-2024
# Course/Section:IS4010
# Semester/Year:Spring/2024
# Brief Description of the assignment:
# Anything else that's relevant:


def stapleet(roman):
    # Create a dictionary to map Roman numerals to their corresponding values
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    # Initialize the result
    result = 0
    
    # Iterate through the Roman numeral from left to right
    for i in range(len(roman)):
        # If the current numeral is smaller than the next numeral, subtract its value
        if i < len(roman) - 1 and roman_values[roman[i]] < roman_values[roman[i + 1]]:
            result -= roman_values[roman[i]]
        else:
            result += roman_values[roman[i]]
    
    return result

if __name__ == "__main__":
    # Example usage
    roman_numeral = "XXVII"
    integer_value = stapleet(roman_numeral)
print(f"The Roman numeral {roman_numeral} is equivalent to {integer_value}.")