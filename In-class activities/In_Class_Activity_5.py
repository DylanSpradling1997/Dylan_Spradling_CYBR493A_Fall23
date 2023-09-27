"""
In class activity 5

"""
import IfStatement
import In_Class_3
import In_Class_4_Pinger
def main():
    userinput = input("Please select from these option. if-activity: enter 1 In_class_activity3: enter 2  InClassActivity4: press 3")
    if userinput == 1:
        IfStatement.number1()
    if userinput == 2:
        In_Class_3.CoolWordsChecker()
    if userinput == 3:
        In_Class_4_Pinger.PingIDs()




