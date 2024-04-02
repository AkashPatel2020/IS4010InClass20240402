#MooreHC.py
# Name:Harrison Moore
# email:Moorehc@mail.uc.edu
# Assignment Number:INCLASS    
# Due Date:04-2-2024
# Course/Section:IS4010
# Semester/Year:Spring/2024
# Brief Description of the assignment:We are using code from leetcode 
# Anything else that's relevant: Solved using ChatGPT


def Moorehc(s: str, t: str) -> bool:
    indexS = [0] * 200 # Stores index of characters in string s
    indexT = [0] * 200 # Stores index of characters in string t
        
    length = len(s) # Get the length of both strings

    if length != len(t): # If the lengths of the two strings are different, they can't be isomorphic
        return False
    
    for i in range(length): # Iterate through each character of the strings
        if indexS[ord(s[i])] != indexT[ord(t[i])]: # Check if the index of the current character in string s is different from the index of the corresponding character in string t
            return False # If different, strings are not isomorphic
        
        indexS[ord(s[i])] = i + 1 # updating position of current character
        indexT[ord(t[i])] = i + 1
    
    return True # If the loop completes without returning false, strings are isomorphic
    
if __name__ == "__main__":
    s = "egg"
    t = "treat"
    print(Moorehc(s, t))