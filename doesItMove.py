#!/usr/bin/env python3

print("\n* * * ENGINEERING FLOWCHART * * *")

i = 0
# created a function to warn user about invalid input


def err():
    print("\nGet it it together ENGENEER! Enter YES or NO")

# quit/escape message


def escape():
    print("\nI'm affraid, it won't be fixed by itself...")


# first question
while i == 0:
    question1 = input("\nDoest it move?")
    if question1.strip().capitalize() == "Q":
        escape()
        break
    elif question1.strip().capitalize() == "Y" or question1.strip().capitalize() == "YES":
        i += 1
        # second question
        while i == 1:
            question2 = input("\nShould it?")
            if question2.strip().capitalize() == "Q":
                break
            elif question2.strip().capitalize() == "Y" or question2.strip().capitalize() == "YES":
                print("\nNo problem1")
                i += 1
            elif question2.strip().capitalize() == "N" or question2.strip().capitalize() == "NO":
                print("\nUse duck tape")
                i += 1
            # 'i' does not increase or decrease, so the question will remain the same
            else:
                err()

    elif question1.strip().capitalize() == "N" or question1.strip().capitalize() == "NO":
        i += 1
        # second question
        while i == 1:
            question2 = input("\nShould it?")
            if question2.strip().capitalize() == "Q":
                escape()
                break
            elif question2.strip().capitalize() == "Y" or question2.strip().capitalize() == "YES":
                print("\nGlue it!")
                i += 1
            elif question2.strip().capitalize() == "N" or question2.strip().capitalize() == "NO":
                print("\nNo problem")
                i += 1
            # i does not increase or decrease, so the question will remain the same
            else:
                err()
    else:
        err()

