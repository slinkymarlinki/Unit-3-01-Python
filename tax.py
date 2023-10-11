#!usr/bin/env python3
# Created By: Marli Peters
# Date: Oct. 11, 2023
# This program asks the user for a subtotal then
# calculates tax for it in Prince Edward Island.
# It then displays the total and tax.
import constants


def main():
    # get user input
    subtotal = float(input("Enter subtotal: $"))

    # calculate tax and total
    tax = subtotal * constants.HST
    total = subtotal + tax

    # display total and tax
    print("")
    print("The Total is ${0:.2f}".format(total))
    print("The Tax is ${0:.2f}".format(tax))


if __name__ == "__main__":
    main()
