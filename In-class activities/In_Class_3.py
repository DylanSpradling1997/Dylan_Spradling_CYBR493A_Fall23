def main():
    print()
    if CoolWordsChecker() == True:
        print("moving to next Functionality")
    else:
        print("Your are stuck here")


def WordsChecker():

    """
    This method checks wether a user input matches a pre-defined password or not
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