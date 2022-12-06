'''
Author: Holden Vail
KUID: 2936812
Date: 2022/09/28
Lab: lab04
Last modified: 2022/09/28
Purpose: The purpose of this program is to help the user keep track of items for their shopping list
'''

shopping = ['']
removing = []
answer = 0
count = 1
goodString = ''
while answer != 4:
    print("\n","=====================================================================")
    print("Welcome to SUPER shopper: The best shopping application on the market ")
    print('',"1) Add item","\n","2) Check off item","\n","3) Print off list","\n","4) Exit","\n")
    answer = int(input("Enter a choice: "))
    if answer == 1:
        shopping.append(input('What item would you like to add to your list?: '))
    elif answer == 2:
        remove = int(input("Please enter the number of the item would you like to check off your list: "))
        remove_string = shopping[remove]
        high = len(remove_string) - 1  #Max letter to erase
        for letter01 in remove_string: #Making new, editable version of word
            removing.append(letter01)
        for letter02 in removing[1:high]: #Erasing letter within range of old word
            removing[1:high] = '-'*(len(remove_string)-2)
        for letter03 in removing:
            goodString += letter03
        removing = []                   #Reassigning and cleaning up variables
        shopping[remove] = goodString
        goodString = ''
    elif answer == 3:
        for letter04 in shopping[1::]:     #Printing in format
            print(f"{count}) {letter04}")
            count += 1
        count = 1
    elif answer != 4:
        print('Please enter a valid response')
print("Goodbye!")