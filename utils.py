
import os
from typing import List, Tuple
import gameState
import random


def clear():
    os.system('cls')


def pocketSpaceLeft(drugs: Tuple[str, int, int], totalPocketSpace: int):
    spaceTaken = 0

    for drug, amount, price in drugs:
        spaceTaken = spaceTaken + amount
    return totalPocketSpace - spaceTaken


def createOptions(options: List[str], question: str):
    optionsText = f'{question} '

    for i, option in enumerate(options):
        if i == len(options)-1:
            optionsText += f'or ({option[0]}){option[1:]}?'
        else:
            optionsText += f'({option[0]}){option[1:]}, '
    print(optionsText)


def selectOption(options: List[str]):
    selectedIndex = None
    while selectedIndex == None:
        userInput = input('Type the entire word > ')

        for i, option in enumerate(options):
            if option.lower() == userInput.lower() or option[0].lower() == userInput.lower():
                selectedIndex = i
                break

        if selectedIndex == None:
            print('incorrect input. type the word... dummy')

    print(f'You chose {options[selectedIndex]}\n')

    return selectedIndex


def randomizeDrug():
    for i, (drug, amount, price) in enumerate(gameState.drugs):
        low = gameState.drugVariance[gameState.currentCity][i][0]
        high = gameState.drugVariance[gameState.currentCity][i][1]
        gameState.drugs[i] = (drug, amount, random.randint(low, high))
