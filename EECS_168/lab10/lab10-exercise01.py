'''
Author: Holden Vail
KUID: 2936812
Date: 2022/12/02
Lab: lab09
Last modified: 2022/12/02
Purpose: The purpose of this program to create a functional prototype of software that could be used in a DMV
'''

from dmv import DMV #brings in all peritnent files
def main():
    DMV("records.txt").interface()   #Runs everything
main()