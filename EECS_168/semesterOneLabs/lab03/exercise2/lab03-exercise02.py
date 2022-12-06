'''
Author: Holden Vail
KUID: 2936812
Date: 2022/09/15
Lab: lab03
Last modified: 2022/09/15
Purpose: This program is a game in which the user must guess a phrase. The program aids the user in guessing.
'''

answer = "bringcoffee"
guess = ""
guess_num = 0
characters = 0
index_count = 0

#primary program
while guess != answer:
    guess_num += 1
    guess = input("Enter a guess: ").lower()
    if len(guess) > len(answer):
        print("Too many characters!")
    elif len(guess) < len(answer):
        print("Too few characters!")
    elif guess != answer:
        for letter in guess:
            if letter == answer[index_count]:
                characters +=1
            index_count += 1
        print(f"You have {characters} correct characters in your guess")
        index_count = 0
        characters = 0

#printing results
print(f"Congratulations, you found the secret word in {guess_num} guesses!")