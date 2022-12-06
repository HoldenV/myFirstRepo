'''
Author: Holden Vail
KUID: 2936812
Date: 2022/10/27
Lab: lab08
Last modified: 2022/10/27
Purpose:
'''
import random

def buildPoke(fileName):
    """This function builds a pokedex from a file containing the names of all the pokemon """
    pokeData = open(fileName, "r")
    pokeDict = {}
    for line in pokeData:
        lineWords = line.split()
        pokeDict[lineWords[0].strip()] = lineWords[1].strip()
    return pokeDict

def buildTeam(pokedex, size=6, isUnique=False):
    """The purpose of this program is to build a random list for a pokemon team"""
    if isUnique == False:
        teamList = random.choices(list(pokedex.keys()), k=size)
    else:
        tempList = []
        for number, name in pokedex.items():
            tempList.append(name)
        teamList = random.sample(tempList, k=size)
    return teamList

def battle(team1,team2):
    """The purpose of this program is to show to pokemon teams fighting and find the victor"""
    count1 = 0
    count2 = 0
    round = 1
    win1 = 0
    win2 = 0
    boarder = 30
    losingTeam = [0, 1]
    losingCount = 0
    if len(team1) != len(team2):
        print("To ensure a fair batle, please ensure that both selected teams have the same amount of pokemon")
    else:
        while losingCount < len(losingTeam):
            print(f"Round {round}".center(boarder,"="))
            print(f"{team1[count1]} VS {team2[count2]}".center(boarder,"+"))
            randChioce = random.randint(1,2)
            if randChioce == 1:
                print(f"{team1[count1]} wins".center(boarder,"="))
                count2 += 1
                win1 += 1
                if win1 > win2:
                    losingTeam = team2
                    losingCount = count2
            if randChioce == 2:
                print(f"{team2[count2]} wins".center(boarder, "="))
                count1 += 1
                win2 += 1
                if win1 < win2:
                    losingTeam = team1
                    losingCount = count1
            print("\n")
            round += 1
        if win1 > win2:
            print("Team 1 wins!!".center(boarder, "="))
        if win1 < win2:
            print(" Team 2 wins!!".center(boarder, "="))
        if win1 == win2:
            print("It's a tie!".center(boarder, "="))

def translate(pokedex, pokeName):
    """The purpose of the is function is to return the translation of the English name of the pokemon"""
    if str(pokeName).strip() in pokedex.keys():
        print(f"The Japanese name for this pokemon is {pokedex[pokeName]}.")
    else:
        print(f"The inputted pokemon does not yet have an entry in the given pokedex")

def main():
    pokedex = buildPoke("pokeData.txt")
    response = 0
    queue = []
    while response != 5:
        print("-------------------------------")
        print("1) Print Pokedex")
        print("2) Translate")
        print("3) Build a team")
        print("4) Pokemon battle")
        print("5) Exit")
        print("-------------------------------")
        response = int(input("Choice: "))
        if response == 1:
            print(pokedex)
        if response == 2:
            englishName = input("Enter the English name of the pokemon: ")
            translate(pokedex, englishName)
        if response == 3:
            size  = int(input("How many pokemon would you like on this team?: "))
            unique = input("Would you like each pokemon on the team to be unique? (Y/N): ").lower()
            if unique == "y":
                unique = True
            if unique == "n":
                unique = False
            currentTeam = buildTeam(pokedex, size, unique)
            queue.append(currentTeam)
            print("\n")
            print(f"You built a team with {currentTeam}")
            print("\n", "\n")
            print("This team has been added to the fight queue. The two most recently added teams will battle.")
            print("The queue is cleared after each battle")
        if response == 4:
            if len(queue) > 1:
                battle(queue[0], queue[1])
                queue = []
            else:
                print("Please add build at least one more pokemon team to begin battling")
    print("Goodbye!!".center(30, "="))

main()