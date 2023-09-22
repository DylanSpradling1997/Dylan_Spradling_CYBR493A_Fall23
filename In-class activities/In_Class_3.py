def main():
    print()
    userinput = input("guess the password")
    if WordsCheckerWithInput(userinput) == True:
        print("Moving to next function")
    else:
        print("hardstuck buddy")


    if CoolWordsChecker() == True:
        print("moving to next Functionality")
    else:
        print("You are stuck here")


def WordsCheckerWithInput(data):
    """
    This method check whether data matches the password
    :param data: This is what is being passed from the outside
    :return: true if data matches, False otherwise
    """
    if (data == "Fluffkinz"):
        return True
    else:
        return False


def WordsChecker():

    """
    This method checks whether a user input matches a pre-defined password or not
    :return:
    """
    secretWord = "Fluffkinz"
    userInput = input("Guess the password")
    if (secretWord == userInput):
        print("You guessed it!")
    else:
        print("You did not guess it")

def CoolWordsChecker():

    """
    This method checks wether a user input matches a pre-defined password or not
    :return:
    """
    secretWord = "Fluffkinz"
    userInput = input("Guess the password")
    if (secretWord == userInput):
        return True
    else:
        return False

if __name__ == "__main__":
    main()