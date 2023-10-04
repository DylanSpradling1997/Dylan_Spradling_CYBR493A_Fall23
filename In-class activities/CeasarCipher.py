import string


def main():
    letters = list(string.ascii_lowercase)

    print(letters)

    plaintext = "wvu".lower()
    encrypted = ""
    key = 4
    counter = 0

    for char in plaintext:
        currentLocation = letters.index(char)

        newLocation = (currentLocation + key)%26

        newChar = letters[newLocation]
        print(char, currentLocation, newLocation,newChar)

if __name__ == "__main__":
    main()