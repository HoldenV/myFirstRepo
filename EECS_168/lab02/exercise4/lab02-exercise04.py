'''
Author: Holden Vail
KUID: 2936812
Date: 2022/09/12
Lab: lab02
Last modified: 2022/09/12
Purpose: This program help intelligently package pop into the fewest possible containers
'''

pop_qty = int(input("How much pop do you have? "))
cubers = pop_qty // 24
not_cubers = pop_qty % 24
sixers = not_cubers // 6
singles = not_cubers % 6

print("Cubes:", cubers)
print("Six-packs:", sixers)
print("Singles:", singles)
