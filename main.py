import utils
import printScreens
import gameState
import random


def yallWantSomeDrugs():
    printScreens.printSplash()
    input()
    utils.randomizeDrug()
    goCity()


def goCity():

    printScreens.printCity()
    print()

    utils.createOptions(['Buy', 'Sell', 'Jet'], 'Would you like to')
    userSelected = utils.selectOption(['Buy', 'Sell', 'Jet'])

    if (userSelected == 0):
        None
    elif (userSelected == 1):
        None
    elif (userSelected == 2):
        goJet()


def goJet():
    utils.createOptions(gameState.cities, 'Where would you like to go')
    userSelected = utils.selectOption(gameState.cities)

    if gameState.currentCity != userSelected:
        utils.randomizeDrug()

        gameState.days = gameState.days - 1
        gameState.currentCity = userSelected

    if gameState.days == 0:
        goGameOver()
    else:
        goCity()


def goGameOver():
    print('See ya Sucker')


yallWantSomeDrugs()
