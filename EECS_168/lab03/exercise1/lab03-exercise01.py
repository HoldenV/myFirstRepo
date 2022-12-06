'''
Author: Holden Vail
KUID: 2936812
Date: 2022/09/15
Lab: lab03
Last modified: 2022/09/15
Purpose: The purpose of this program is to help the user compare two strings for a match (case sensitive or not)
'''

response = ""

#User Inputs
input_string = input("Enter a string: ")
response = input("Do you want a case-sensitive match? (Y/N): ").lower()
sequence = input("Enter the sequence you want to search for: ")

# Case-Sensitivity
if response == 'n':
    input_string = input_string.lower()
    sequence = sequence.lower()

# Finding matches
total = input_string.count(sequence)

# Printing Result
print(f"Matches: {total}")