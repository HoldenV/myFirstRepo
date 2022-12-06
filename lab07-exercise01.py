'''
Author: Holden Vail
KUID: 2936812
Date: 2022/10/25
Lab: lab03
Last modified: 2022/10/25
Purpose: The purpose of this program is to help the user transform and work with numbers
'''

def cleanWord(word):
    """The purpose of this funcion is to remove all punctuation from given word"""
    punc = [",", ".", "?", "!", ":", ";", "(", ")", "[", "]", '"', "-"]
    newWord = ""
    for letter in word:
        if letter not in punc:
            newWord += letter.lower()
    return newWord.strip()

def buildCount(fileName):
    "The purpose of this program is to build a dicitonary with the counts for word usuage in a given file"
    constFile = open(fileName, "r")
    wordList = []
    lineList = []
    dirtyList = []
    for each in constFile:                              #Breaks apart words using lists
        lineList.append(each.strip())
    for each in lineList:
        dirtyList.append(each.split(" "))
    for each in dirtyList:
        for word in each:
            wordList.append(cleanWord(word))

    constDict = {}                          #Makes dictionary using lists built above
    for each in wordList:
        if each in constDict:
            constDict[each] += 1
        else:
            constDict[each] = 1
    return constDict

def uniqueWords(dictName):
    uniqueList = []
    for word, occurance in dictName.items():
        if occurance == 1:
            uniqueList.append(word)
    return uniqueList

def main():
    """This program contains all the major funcitons and interfacing for the program"""
    welcome = " Welcome to the Worder! ™ "
    print(welcome.center(60,"="))
    fileName = input("Please enter the name of the file you wish to process: ").strip()

    constDict = buildCount(fileName)
    uniqueList = uniqueWords(constDict)

    word_data = open("word_data.txt", "w")
    unique_words = open("unique_words.txt", "w")

    for word, occurance in constDict.items():
        word_data.write(f"Word: {word}, Occurances: {occurance} \n")
    for word in uniqueList:
        unique_words.write(f"{word} \n")

    word_data.close()
    unique_words.close()

    print("============================================================")
    print(f"The file {fileName} has been processed")
    print("Output stored in word_data.txt and unique_words.txt")
    print("Exiting..........")

main()