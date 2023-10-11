import string

"""
Dylan Spradling
IN class activity 7
10/11/2023
CYBR 493A
"""


def main():
    letters = list(string.ascii_lowercase)

    plaintext = "Dynamite".lower()
    x = 0
    cyphertext = ""
    for char in plaintext:
        # assigns number to x
        x = letters.index(char)

        # takes x and cyphers it using formula below
        dacipher = (x + 4 + 32 + 18)

        # Im not sure if this is necessary but it works
        hidden = dacipher

        # gets new location
        newlocation = hidden % 25

        # modifier so the text can be de-cypher by multiplying it by 25 x times
        modifier = int(hidden / 25)

        # get new character with newlocation number
        newChar = letters[newlocation]

        # stores new letters in a string for readability
        cyphertext = cyphertext + newChar

        # prints out original word, cyphered word and the modifier when the loop is finished
        if len(plaintext) == len(cyphertext):
            print(plaintext, cyphertext, modifier)


if __name__ == "__main__":
    main()
