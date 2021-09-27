#Tic-Tac-Tie - Clean.py - A tic-tac-toe game that displays a grid, allows you to choose a spot and then displays your choice on a board
#Also keeps track of the score

import copy
import time
import random
import sys

##Board design to make it look pretty
def printBoard(board):
    print('')
    print(board['top-l'] + '|' + board['top-m'] + '|' + board['top-r'])
    print('-----')
    print(board['mid-l'] + '|' + board['mid-m'] + '|' + board['mid-r'])
    print('-----')
    print(board['low-l'] + '|' + board['low-m'] + '|' + board['low-r'])
    print('')

##Function for initiating the board back to blank
def blankBoard(zeroBoard):
    for value in zeroBoard:
        zeroBoard[value] = ' '

##Function for initiating a New Game after a game over situation
def newGame(YorN):
    print('\n ~ Would you like to play again? if yes, type ''Y'': ~ ')
    newGame = input()
    if newGame.upper() == 'Y':
        print(' ~ okay, please wait while we set up a new game! ~ ')
        blankBoard(theBoard)
        time.sleep(random.randint(1,2))
        printBoard(theBoard)
    else:
        print('\n ~ Bye and thank you for playing!! ~ ')
        sys.exit()        

##Function containing all the win conditions
def winCondition(winner):
    if ((winner['top-l'] == winner['top-m'] == winner['top-r'] == 'X') or
    (winner['mid-l'] == winner['mid-m'] == winner['mid-r'] == 'X') or
    (winner['low-l'] == winner['low-m'] == winner['low-r'] == 'X') or
    (winner['top-l'] == winner['mid-l'] == winner['low-l'] == 'X') or
    (winner['top-m'] == winner['mid-m'] == winner['low-m'] == 'X') or
    (winner['top-r'] == winner['mid-r'] == winner['low-r'] == 'X') or
    (winner['top-l'] == winner['mid-m'] == winner['low-r'] == 'X') or
    (winner['top-r'] == winner['mid-m'] == winner['low-l'] == 'X')):
        print('\n ~ Congratulations! You are a winner!  ')
        return 'win'


##Function containing all the loss conditions
def loseCondition(loser):
    if ((loser['top-l'] == loser['top-m'] == loser['top-r'] == 'O') or
    (loser['mid-l'] == loser['mid-m'] == loser['mid-r'] == 'O') or
    (loser['low-l'] == loser['low-m'] == loser['low-r'] == 'O') or
    (loser['top-l'] == loser['mid-l'] == loser['low-l'] == 'O') or
    (loser['top-m'] == loser['mid-m'] == loser['low-m'] == 'O') or
    (loser['top-r'] == loser['mid-r'] == loser['low-r'] == 'O') or
    (loser['top-l'] == loser['mid-m'] == loser['low-r'] == 'O') or
    (loser['top-r'] == loser['mid-m'] == loser['low-l'] == 'O')):
        print('\n ~ Aww man, you''re are a loser! ~ ')
        return 'lose'
 

##Function for Computer Players Choice
def computerChoice(cpuChoice):
    theBoardCPU = copy.deepcopy(theBoardChoices)
    print(','.join(theBoardCPU.keys()))
    cpuChoice = random.choice(list(theBoardCPU.keys()))
    print(' ~ ' + cpuChoice + ' ~ ')
    del theBoardChoices[cpuChoice]
    theBoard[cpuChoice] = 'O'
    printBoard(theBoard)



##Blank board to begin with and making a copy of the board for choices remaining, and finally printing a pretty board
theBoard = {'top-l': ' ', 'top-m': ' ', 'top-r': ' ',
	    'mid-l': ' ', 'mid-m': ' ', 'mid-r': ' ',
	    'low-l': ' ', 'low-m': ' ', 'low-r': ' '}
theBoardChoices = copy.deepcopy(theBoard)
printBoard(theBoard)

##The actual game
print(' ~ Hello player. What is your name? ~ ')
player1Name = input()
print(' ~ Hello ' + player1Name + ', welcome to tic-tac-toe ~ ')
playerScore = 0
CPUScore = 0

while theBoardChoices != None:
    print(' ~ ' +player1Name + ', please type in one of the options for blank spaces: ~ ')
    print('')
    print(' , '.join(theBoardChoices.keys()))
    playerInput = input()
    playerChoice = playerInput.lower()
    choiceCheck = theBoard.get(playerChoice,'bad choice')
    
    if choiceCheck != 'bad choice':
        
        if theBoard[playerChoice] == ' ':
            theBoard[playerChoice] = 'X'
            printBoard(theBoard)
            del theBoardChoices[playerChoice]
            if winCondition(theBoard) == 'win':
                theBoardChoices = copy.deepcopy(theBoard)
                playerScore = playerScore + 1
                print('  ~  the current score is ' + str(playerScore) +'-' + str(CPUScore) + '  ~  ')
                newGame(theBoardChoices)
                continue
            if theBoardChoices == {}:
                theBoardChoices = copy.deepcopy(theBoard)
                newGame(theBoardChoices)
                continue               
            print(' ~ Please wait. Computer making a choice... ~ ')
            time.sleep(random.randint(1,2))
            computerChoice(theBoard)
            if loseCondition(theBoard) == 'lose':
                theBoardChoices = copy.deepcopy(theBoard)
                CPUScore = CPUScore + 1
                print('  ~  the current score is ' + str(playerScore) +'-' + str(CPUScore) + '  ~  ')
                newGame(theBoardChoices)
                continue             
            
        else:
            print(' ~ that space is already taken ~ ')
