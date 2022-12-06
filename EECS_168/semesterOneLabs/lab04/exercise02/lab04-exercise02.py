'''
Author: Holden Vail
KUID: 2936812
Date: 2022/09/28
Lab: lab04
Last modified: 2022/09/28
Purpose: The purpose of this program is to provide the user with statistics about the two given lists
'''

sumWin = ""
sumNum = 0
avgWin = ""
avgNum = 0
matches = 0
palindrome = "aren't"
irregular = False
list1 = []
list2 = []

file1Name =input("What is the name of the first file?: ").strip()      #Gather inputs
file2Name = input("What is the name of the second file?: ").strip()

file1 = open(file1Name,"r")     #Opening files
file2 = open(file2Name, "r")

for line in file1:
    list1.append(int(line.strip()))
for line in file2:
    list2.append(int(line.strip()))

if list1[::] == list2[::-1] or list1[::] == list2[::]:                                     #Check for irregular cases
    irregular = True

for number in list1:                                              #Matches tally
    matches += list2.count(number)

if irregular == True:                                       #Print irregular results
    palindrome = "are"
    print("======================")
    print("List statistics: ")
    print(f"The sums of both lists are equal and {str(sum(list1))}")
    print(f"the averages of both lists are equal and {str(sum(list1)/len(list1))}")
    print(f"Number of times a number appears on both lists: {matches}")
    print(f"The lists {palindrome} palindromes.")

while irregular == False:
    if sum(list1) > sum(list2):     #Finding out which list has the larger sum and what that sum is
        sumWin = "first"
        sumNum = sum(list1)
    if sum(list1) < sum(list2):
        sumWin = "second"
        sumNum = sum(list2)

    if sum(list1)/len(list1) > sum(list2)/len(list2):       #Calculate / display averages
        avgWin = "first"
        avgNum = sum(list1)/len(list1)

    if sum(list1)/len(list1) < sum(list2)/len(list2):
        avgWin = "second"
        avgNum = sum(list2)/len(list2)

    print("======================")                             #Print regular results
    print("List statistics: ")
    print(f"The {sumWin} list has the larger sum of {sumNum}")
    print(f"The {avgWin} list has the larger average of {avgNum:.1f}")
    print(f"Number of times a number appears on both lists: {matches}")
    print(f"The lists {palindrome} palindromes.")
    irregular = True

file1.close()
file2.close()