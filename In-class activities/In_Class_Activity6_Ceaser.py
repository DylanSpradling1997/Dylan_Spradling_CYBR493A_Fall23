import string
"""
Dylan Spradling
9/28/2023
In class activity 6
This program print out the name of the creator in both plaintext and in cypher text 
"""



def main():
    letters = list(string.ascii_lowercase)

    print(letters)

    plaintext = "dylan".lower()
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