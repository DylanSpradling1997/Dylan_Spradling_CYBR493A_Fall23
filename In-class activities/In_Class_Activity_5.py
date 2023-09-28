"""
Dylan Spradling
9/28/2023
In class activity 5
This program prompts the user for input then calls the desired activity based on the user input
"""
import IfStatement
import In_Class_3
import In_Class_4_Pinger


def main():
    userinput = input(
        "Please select from these option. if-activity: enter 1 In_class_activity3: enter 2  InClassActivity4: press 3")
    if userinput == 1:
        return IfStatement
    if userinput == 2:
        return In_Class_3
    if userinput == 3:
        return In_Class_4_Pinger
