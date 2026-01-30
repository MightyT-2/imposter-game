from os import system, listdir
from platform import system as os

inputPlayers  = ''
playerList    = []
imposterCount = 0
inputCount    = ''
dictList      = list(x[:-4] for x in listdir('dictionaries') if x[-4:] == '.txt')
index         = 0
indexSelector = ''
userIndex     = 0
currentFile   = ''
wordCount     = 0

class Player:
    playerCount = 0

    def __init__(this, playerName):
        this.name = playerName
        this.isImposter = False
        this.score = 0
        this.playerId = Player.playerCount
        Player.playerCount += 1
    
    def setImposter(this):
        this.isImposter = True
        return

    def reset(this):
        this.isImposter = False
        return
    
    def getId(this):
        return this.playerId

def clearScreen():
    if os() == 'Windows':
        system('cls')
    else:
        system('clear')

if __name__ == "__main__":

    # Get the player list
    inputPlayers = ''
    while inputPlayers != '!done':
        inputPlayers = input('Enter player name: ')
        if inputPlayers != '!done':
            playerList.append(Player(inputPlayers.strip()))
            print(playerList[len((playerList)) - 1].getId())
    clearScreen()

    # Get the imposter count
    while imposterCount <= 0 or imposterCount > len(playerList) / 2:
        try:
            imposterCount = int(input(f'How many imposters do you want (player count: {len(playerList)}): '))
            if imposterCount <= 0:
                print('You need more than 0 imposters!')
            if imposterCount > len(playerList) / 2:
                print('You need less than half the player count as imposter!')
        except:
            print('Not a valid number!')
    clearScreen()

    # Get the category
    index         = 0
    indexSelector = ''
    userIndex     = -1
    print('Select a category.')
    for x in dictList:
        wordCount = len(open('dictionaries\\' + x + '.txt', 'r').read().split('\n'))
        print(f" {index}) {x} ({wordCount})")
        index += 1
    while userIndex <= -1 or userIndex >= index:
        indexSelector = input(' >> ')
        try:
            userIndex = int(indexSelector)
        except:
            userIndex = -1
    currentFile = dictList[userIndex]
    clearScreen()

    #