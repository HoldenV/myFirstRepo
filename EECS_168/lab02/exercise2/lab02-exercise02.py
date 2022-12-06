'''
Author: Holden Vail
KUID: 2936812
Date: 2022/09/12
Lab: lab02
Last modified: 2022/09/12
Purpose: This program completes a long division problem for the user and outputs a response with a remainder instead of decimal
'''

numerator = int(input("Numerator?"))
denominator = int(input("Denominator?"))

if denominator == 0:
    print("You can't divide by zero!")
else:
    int_div_answer = numerator // denominator 
    remainder_answer = numerator % denominator 

    print(numerator,"/",denominator,"=", int_div_answer,"remainder",remainder_answer)