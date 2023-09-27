"""
Dylan Spradling
Homework 2
9/24
Cyber 493A
A file that creates the methods used in HW2_main
"""


def ValidLength(userinput):
    if len(userinput) >= 8:
        return True
    else:
        return False


def HasNumber(userinput):
    for x in userinput:
        if x.isnumeric():
            return True
        else:
            return False

#@MJ: This method does not work correctly.
#see answer key
def HasSymbol(userinput):
    specChars = ["!", "@", "#", "$", "%", "*"]
    for x in userinput:
        for y in specChars:
            if x == y:
                return True

        return False

