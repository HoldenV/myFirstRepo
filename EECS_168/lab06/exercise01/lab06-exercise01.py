'''
Author: Holden Vail
KUID: 2936812
Date: 2022/10/07
Lab: lab03
Last modified: 2022/10/07
Purpose: The purpose of this program is to help the user transform and work with numbers
'''

def last_digit(num):
    """The function returns the last digit of a number"""
    return int(list(str(num)).pop())

def remove_last_digit(num):
    """This function returns the input number without the last digit"""
    return int(str(num)[0:len(str(num))-1])

def add_digit(num, add_digit):
    """This function returns the first number times 10 and with the second input digit added to it"""
    return int(str(num)+str(add_digit))

def reverse(num):
    """This funciton returns a reversed version of the original number"""
    copyNum = num
    counter = 0
    newNum = ""
    while counter < len(str(copyNum))-1:
        lastDigit = last_digit(num)
        num = remove_last_digit(num)
        newNum = add_digit(newNum,lastDigit)
        counter += 1
        if len(str(num)) == 1:
            newNum = add_digit(newNum,num)
    return newNum

def is_palindrome(num):
    """This function returns a T/F if the input number is a palindrome"""
    return num == reverse(num)

def count_digits(num):
    """This program counts the number of digits in an input"""
    copyNum = num
    counter = 0
    for each in str(num):
        if type(remove_last_digit(copyNum)) == type(counter):
            counter += 1
    return counter

def sum_digits(num):
    """This funciton sums all the digits in the input number"""
    copyNum = num
    sumNum = 0
    counter = 0
    for each in str(num):
        if len(str(copyNum)) == 1:
            sumNum += copyNum
        else:
            lastDigit = last_digit(copyNum)
            copyNum = remove_last_digit(copyNum)
            sumNum += lastDigit
            counter += 1
    return sumNum

def print_menu():
    """This function prints the user menu"""
    print("===========================")
    print("1) Count digits")
    print("2) Sum digits")
    print("3) Is palindrome")
    print("4) Reverse")
    print("5) Exit")
    print("===========================")

def main():
    """This is the main program that utilizes the other functions and provides the user with an interactive program"""
    choice = 0
    while choice != 5:
        print_menu()
        choice  = int(input("Choice: "))
        if choice != 5:
            inNum = int(input("Number?: "))
            toPrint = ""
            if choice == 1:
                toPrint = count_digits(inNum)
            elif choice == 2:
                toPrint = sum_digits(inNum)
            elif choice == 3:
                toPrint = is_palindrome(inNum)
            elif choice == 4:
                toPrint = reverse(inNum)
            print("===========================")
            print(toPrint)
        else:
            print("===========================")
            print("Goodbye!")
            print("===========================")

main()
