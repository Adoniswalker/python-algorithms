# Have the function CodelandUsernameValidation(str) take the str parameter being passed and determine if the string is a valid username according to the following rules:
#
# 1. The username is between 4 and 25 characters.
# 2. It must start with a letter.
# 3. It can only contain letters, numbers, and the underscore character.
# 4. It cannot end with an underscore character.
#
# If the username is valid then your program should return the string true, otherwise return the string false.
# Examples
# Input: "aa_"
# Output: false
# Input: "u__hello_world123"
# Output: true
# import re
import string


def CodelandUsernameValidation(strParam):
    le = len(strParam)
    if le > 25 or le < 4:
        return False
    if strParam[0] not in string.ascii_letters or strParam[le - 1] == '_':
        return False
    char = set(string.ascii_letters + string.digits + '_')
    for item in strParam:
        if item in char:
            pass
        else:
            return False
    return True


print(CodelandUsernameValidation("aa_"))
print(CodelandUsernameValidation("u__hello_world123"))
