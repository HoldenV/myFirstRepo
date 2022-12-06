'''
Author: Holden Vail
KUID: 2936812
Date: 2022/09/15
Lab: lab03
Last modified: 2022/09/15
Purpose: The purpose of this program is to help the user calculate how many people will be sick for any given day with the given rules
'''

day = int(input("What day do you want a sick count for?: "))

#First three days need to be treated differnently because they are not preceded by other days to add together

three_days_back = 1
two_days_back = 4
one_day_back = 64
if day > 0:
    if day == 1:
        total = three_days_back
    if day == 2:
        total = two_days_back
    if day == 3:
        total = one_day_back

# All days 4 and greater will be added up by creating a new sum for each day.

    if day >= 4:
        while day >= 4:
            total = three_days_back + two_days_back + one_day_back
            three_days_back = two_days_back
            two_days_back = one_day_back
            one_day_back = total
            day -= 1
    print(f"Total people with flu: {total}")
else:
    print("Please input a valid day: ")