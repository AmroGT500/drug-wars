import utils
import printScreens
import gameState
from splash import logo

utils.clear()

print(logo)

input()

printScreens.printCity()

print()

utils.createOptions(['Buy', 'Sell', 'Jet'], 'Would you like to')
userSelected = utils.selectOption(['Buy', 'Sell', 'Jet'])

if (userSelected == 2):
    utils.createOptions(gameState.cities, 'Where would you like to go')
