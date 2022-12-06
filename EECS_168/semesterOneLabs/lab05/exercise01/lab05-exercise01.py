'''
Author: Holden Vail
KUID: 2936812
Date: 2022/09/28
Lab: lab03
Last modified: 2022/09/29
Purpose: The purpose of this program is to emulate a web history logger
'''
selector = -1
pageCount = -1
leave = False
arrow = ""
historyList = []
commandList = ""
command = ""

while leave != True:
    commandList = input("Enter a command: ").split(" ")                     #Set loop, inputs, and variables
    if commandList[0] == "NAVIGATE" and len(commandList) == 2:              #Nav functions
        historyList = historyList[0:selector + 1]
        historyList.append(commandList[1])
        selector += 1
        pageCount += 1
    if commandList[0] == "BACK":                                              #Back function
        if selector > 0:
            selector -= 1
    if commandList[0] == "HISTORY":                                         #History feature
        print("\n","Oldest")
        print("=========================")
        for each in historyList:
            if each == historyList[selector]:
                arrow = "<--"
            print(f"{each} {arrow}")
            arrow = ""
    if commandList[0] == "EXIT":                                            #Exit clause
        leave = True
    commandList = ""