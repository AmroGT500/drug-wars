import gameState
import utils


def printDrugs():
    print(f'{"Drug":10} {"Inventory":^10}{"Price":>10}')
    print('─'*31)
    for drug, amount, price in gameState.drugs:
        print(f'{drug:10}{amount:^10d}{price:10d}')
    print()


def printStats():
    for key, value in gameState.stats.items():
        print(key, value, end='  |  ')
    print('\n')


def printCity():
    utils.clear()
    print()
    print(f'Current City: {gameState.cities[gameState.currentCity]}', ' | ',
          f'Days Left: {gameState.days}', ' | ', f'Pocket Space: {gameState.pocket}', ' | ')
    print()
    printStats()
    printDrugs()
