'''
Author: Holden Vail
KUID: 2936812
Date: 2022/09/12
Lab: lab02
Last modified: 2022/09/12
Purpose: This program helps aid the payment process at a restaurant by automatically calculating a cusotmers ticket
'''

print("\n","\n","\n=========================","\nWELCOME TO THE RESTAURANT","\n=========================","\n", "\n","\n")

per_pie_price = 3
pasta_qty = 0
grilled_cheese_qty = 0
pie_qty = 0
customer_age = 0
pasta_total_cost = 0
grilled_cheese_total_cost = 0
pie_total_cost = 0
discount = 0

pasta_input = input("Would you like pasta? (Y/N) ")
if pasta_input == "y" or pasta_input == "Y":
    pasta_qty = int(input("How many? "))

grilled_cheese_input = input("Would you like a grilled cheese? (Y/N) ")
if grilled_cheese_input == "y" or grilled_cheese_input =="Y":
    grilled_cheese_qty = int(input("How many? "))

pie_input = input("Would you like a pie? (Y/N) ")
if pie_input == "y" or pie_input == "Y":
    pie_qty = int(input("How many? "))

customer_age = int(input("How old are you? "))

print("\n","\n","    RECEIPT    ","\n","=========================")
if pasta_qty > 0:
    pasta_total_cost = pasta_qty * 2.5
    print(pasta_qty,f"pasta @ 2.50 ==> {pasta_total_cost:.2f}")
if grilled_cheese_qty > 0:
    grilled_cheese_total_cost = grilled_cheese_qty * 5.55
    print(grilled_cheese_qty,f"grilled cheese @ 5.55 ==> {grilled_cheese_total_cost:.2f}")
if 0 < customer_age <= 5:
    per_pie_price = 0
if pie_qty > 0:
    pie_total_cost = pie_qty * per_pie_price
    print(pie_qty,f"pie @ 3.00 ==> {pie_total_cost:.2f}")
subtotal = pie_total_cost+grilled_cheese_total_cost+pasta_total_cost
print("=========================")
print(f"Subtotal: {subtotal:.2f}")
if customer_age >= 55:
    discount = subtotal*.55
    print(f"Discount: {discount:.2f}")
tax = subtotal*0.08
print(f"Tax:{tax:.2f}")
print("=========================")
total = subtotal-discount+tax
print(f"{total:.2f}")
