
import sys
from MaxConnect4Game import *

def oneMoveGame(currentGame):
    if currentGame.pieceCount == 42:    # Is the board full already?
        print ('BOARD FULL\n\nGame Over!\n')
        sys.exit(0)

    currentGame.aiPlay() # Make a move (only random is implemented)

    print ('Game state after move:')    
    currentGame.printGameBoard()

    currentGame.countScore()
    print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))

    currentGame.printGameBoardToFile()
    currentGame.gameFile.close()


def interactiveGame(currentGame,player):
    
    if player == 'human-next':
        while currentGame.getPieceCount() != 42:
            uMove = int(input('It is your turn...Enter a column number 1 through 7:'))
            if uMove<1 or uMove>7:
                print('Invalid column number, enter a valid column')
                continue
            if not currentGame.playPiece(uMove-1):
                print('Column is full, try another column')
                continue
            try:
                currentGame.gameFile = open("human.txt", 'w')
            except:
                sys.exit('Couldnt find the file')
            
            print ('Game state after move')
            currentGame.printGameBoard()
            currentGame.countScore()
            print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))
            currentGame.printGameBoardToFile()
            currentGame.gameFile.close()

            if currentGame.currentTurn == 1:
                currentGame.currentTurn == 2
            elif currentGame.currentTurn == 2:
                currentGame.currentTurn ==1

            if currentGame.getPieceCount() == 42:
                print ('BOARD FULL\n\n Game Over!\n')
                currentGame.printGameBoard()
                currentGame.countScore()
                print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))
                

            else:
                currentGame.aiPlay()
                try:
                    currentGame.gameFile = open("human.txt", 'w')
                except:
                    sys.exit('Couldnt find the file')
                print('Game State after move')
                currentGame.printGameBoard()
                currentGame.countScore()
                print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))        
                currentGame.printGameBoardToFile()
                currentGame.gameFile.close()
                interactiveGame(currentGame,'human-next') 

    else:
        currentGame.aiPlay()
        try:
            currentGame.gameFile = open("human.txt", 'w')
        except:
            sys.exit('Couldnt find the file')
        print('Game State after move')
        currentGame.printGameBoard()
        currentGame.countScore()
        print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))                        
        currentGame.printGameBoardToFile()
        currentGame.gameFile.close()
        interactiveGame(currentGame,'human-next')
    
    
    if currentGame.getPieceCount() == 42:
        if currentGame.player1Score > currentGame.player2Score:
            print('Result: Player 1 Wins!!!')
            sys.exit(0)
        elif currentGame.player1Score < currentGame.player2Score:
            print('Result: Player 2 Wins!!!')
            sys.exit(0)
        else:
            print('The game resulted in a draw')
            sys.exit(0)        



def main(argv):
   
    if len(argv) != 5:
        print ('Four command-line arguments are needed:')
        print('Usage: %s interactive [input_file] [computer-next/human-next] [depth]' % argv[0])
        print('or: %s one-move [input_file] [output_file] [depth]' % argv[0])
        sys.exit(2)

    game_mode, inFile = argv[1:3]

    if not game_mode == 'interactive' and not game_mode == 'one-move':
        print('%s is an unrecognized game mode' % game_mode)
        sys.exit(2)

    currentGame = maxConnect4Game() # Create a game

    try:
        currentGame.gameFile = open(inFile, 'r')
    except IOError:
        sys.exit("\nError opening input file.\nCheck file name.\n")

    file_lines = currentGame.gameFile.readlines()
    currentGame.gameBoard = [[int(char) for char in line[0:7]] for line in file_lines[0:-1]]
    currentGame.currentTurn = int(file_lines[-1][0])
    currentGame.gameFile.close()
    currentGame.depth=argv[4]

    print ('\nMaxConnect-4 game\n')
    print ('Game state before move:')
    currentGame.printGameBoard()

    currentGame.checkPieceCount()
    currentGame.countScore()
    print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))

    if game_mode == 'interactive':
        interactiveGame(currentGame,argv[3]) # Be sure to pass whatever else you need from the command line
    
    else: 
        outFile = argv[3]
        try:
            currentGame.gameFile = open(outFile, 'w')
        except:
            sys.exit('Error opening output file.')
        oneMoveGame(currentGame)


if __name__ == '__main__':
    main(sys.argv)

