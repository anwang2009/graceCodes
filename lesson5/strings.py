"""
Lesson 5: Doing stuff with strings
"""

# TODO 2: Define a function more_consonants that takes a string and
# returns True if the string has more consonants
# than vowels.
def more_consonants(string):
    vowel = 0
    consonant = 0
    for i in range(0, len(string)):
        letter = string[i]
        if letter == "a":
            vowel += 1
        elif letter == "e":
            vowel += 1
        elif letter == "i":
            vowel += 1
        elif letter == "o":
            vowel += 1
        elif letter == "u":
            vowel += 1
        elif letter == "y":
            vowel += 1
        else:
            consonant += 1
        
    # print(consonant)
    # print(vowel)
    if consonant > vowel:
        return True
    else: 
        return False


# TODO 3: Define a function is_palindrome that takes a string and
# returns True if the string is a palindrome,
# and False otherwise.
def is_palindrome(string):
    reverse = ""
    for i in range(len(string)-1, -1, -1):
        reverse += string[i]
    if reverse == string:
        return True
    else:
        return False

# TODO 4: Define a function `matches` that takes two strings and
# returns True if the strings match each other in the following
# way: '*' represents any single character.
# a*rdvark matches aardvark
# hi matches hi
# *i matches h*
# ol* doesn't match el*
# **** matches ****
# *** doesn't match *
# Returns False if the strings don't match
def matching(string, otherstr):
    if len(string) == len(otherstr):
        for i in range(0, len(string)):
            if string[i] == otherstr[i]:
                continue
            elif string[i] == "*":
                continue
            elif otherstr[i] == "*":
                continue
            else:
                return False
        return True
    else: 
        return False

# TODO 1: Write the main entry point that calls the
# following functions with a few test cases each:
# - is_palindrome
# - more_consonants
# - matches
# 
# Hint: You can print the result of each test, or you can use
# the keyword `assert`, which expects the expression after it to
# evaluate to True
# 
# Printing:
#    result = is_palindrome("racecar")
#    print("is_palindrome of racecar is", result)
#
# Asserting:
#    assert is_palindrome("racecar")
#    assert not is_palindrome("not a palindrome haha")
if __name__ == "__main__":
    assert not more_consonants("onomatopoeia")
    assert more_consonants("palindrome")
    assert is_palindrome("tacocat")
    assert not is_palindrome("spotty")
    assert matching("eoi", "eoi")
    assert not matching("asdfghjkl;", "arstdhneio")
    assert matching("a****h****", "arstd*neio")
    assert not matching("Mathisawesome", "**tdjakfd")