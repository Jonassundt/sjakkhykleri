import random
import copy
from Pieces.Rook import Rook
from Pieces.King import King
from Pieces.Bishop import Bishop
from Pieces.Queen import Queen
from Pieces.Pawn import Pawn
from Pieces.Knight import Knight

"""Chess-game"""

class ChessGame():

    def __init__(self, board):
        self.board = board

    def runGame(self): #create this method later.
        pass

    def getKingPos(self, color):
        return self.board.getKingPos(color)

    def makeMove(self, move): #Only works when input is a move in the list of moves.
        #makes a move on the board and updates the pieces.
        startPos = move[0:2]
        endPos = move[2:4]
        startPiece = self.board.getPiece(startPos)

        #Pawn will transform to a queen if it reaches the end of the board
        if(isinstance(startPiece, Pawn)):
            if(startPiece.color == 'white' and startPos[1:2] == '6'):
                #transform to a queen
                newQueen = Queen(123, self.board, 'white', endPos)
                self.board.setPiece(newQueen, endPos)
                self.board.setPiece('o', startPos)
            elif(startPiece.color == 'black' and startPos[1:2] == '1'):
                #do same as above, just for black queen
                newQueen = Queen(321, self.board, 'black', endPos)
                self.board.setPiece(newQueen, endPos)
                self.board.setPiece('o', startPos)
            else:
                self.board.setPiece(startPiece, endPos)
                self.board.setPiece('o', startPos)
        else:
            self.board.setPiece(startPiece, endPos)
            self.board.setPiece('o', startPos)

    def getPlayerMoves(self, playerColor, checkSelfCheck=1):
        #returns all possible moves on the board [XXXX, XXXY, XXXZ, ...]
        #goes for each piece in the game and adds moves to the list
        playerMoves = [] #tmp moves that seem to be legal
        resultMoves = [] #actual legal moves that are a subset of playerMoves

        #går inn for hver brikke på brettet og samler trekk fra hver brikke.
        for x in range(8):
            for y in range(8):
                piece = self.board.getPiece(str(x) + str(y))
                if(piece != None and piece != 'o'): #sjekker at det er en brikke.
                    if(piece.color == playerColor):
                        pieceMoves = piece.getMoves()
                        for move in pieceMoves:
                            playerMoves.append(move) #adder hver move
        if checkSelfCheck == 0:
            return playerMoves

        # if(checkSelfCheck == 1):
        #     if(playerColor == 'white'):
        #         opposite = 'black'
        #     elif(playerColor == 'black'):
        #         opposite = 'white'

        #doing the self check, because obviously player cannot make move where its putting itself in check.
        for move in playerMoves:
            startPos = move[0:2]
            endPos = move[2:4]
            startPiece = self.board.getPiece(startPos)
            endPiece = self.board.getPiece(endPos)

            #making the move
            self.makeMove(move)
            # self.board.setPiece(startPiece, endPos)
            # self.board.setPiece('o', startPos)

            ###-----------------------------------###
            #looks through all opponents moves to see if itself is in check.
            
            if(self.isPlayerCheck(playerColor) == False): #see if playerColor is in check
                resultMoves.append(move)
            else: #if player is in check after making the move then it cannot make the move, and will not append it
                pass
            #does undo of the move after it has been done.
            self.board.setPiece(startPiece, startPos)
            self.board.setPiece(endPiece, endPos)
        return resultMoves
    

    def isPlayerCheck(self, playerColor):
        #goes through opposite players moves and checks if any moves results in the kings position.
        if(playerColor == 'white'):
            for move in self.getPlayerMoves('black', 0):
                # print("holllaa")
                # print(move) #printing the moves to see if they can take the king.
                if move[2:4] == self.getKingPos('white'):
                    return True
            return False
        
        #do same for black
        elif(playerColor == 'black'):
            # print("im here")
            # print(self.getPlayerMoves('white', 0))
            for move in self.getPlayerMoves('white', 0):
                # print(move + " and " + move[2:4])
                if move[2:4] == self.getKingPos('black'):
                    return True
            return False

    def isCheckMate(self, playerColor):
        #if player has no moves left and it is his turn, then he is checkmate.
        if (len(self.getPlayerMoves(playerColor)) == 0):
            return True
        return False

class Board():
    """Only holds the board with the pieces"""
    def __init__(self):
        self.board = [["o" for i in range(8)] for j in range(8)]
        self.kingPosWhite = '40' #sample position
        self.kingPosBlack = '47' #sample position
    
    def getPiece(self, pos): #returns what piece is at a position, or None.
        #if piece is outside under or to the left of board.
        if("-" in pos):
            return None
        x = int(pos[0])
        y = int(pos[1])

        try:
            piece = self.board[y][x]
        except: #if piece is outside to the right or over
            piece = None
        return piece
    
    def addPiece(self, piece):
        x = int(piece.pos[0])
        y = int(piece.pos[1])
        self.board[y][x] = piece
    
    def getKingPos(self, color):
        #return the position of the chosen king color.
        if(color == 'white'):
            return self.kingPosWhite
        return self.kingPosBlack

    def setPiece(self, piece, pos): #sets a piece on a square position (might be Piece, or 'o')
        y = int(pos[1])
        x = int(pos[0])
        if(piece == 'o'):
            self.board[y][x] = 'o'
        elif(isinstance(piece, King)):
            piece.pos = pos
            self.addPiece(piece)
            #set the king position
            if(piece.color == 'white'):
                self.kingPosWhite = pos
            else:
                self.kingPosBlack = pos

        else:
            piece.pos = pos
            self.addPiece(piece)

    def toString(self): #displays the board
        tmpStr = ''
        for y in self.board:
            row = ''
            for elem in y:
                if elem != 'o':
                    row += elem.toString()
                else:
                    row += elem
            tmpStr = '\n' + row + tmpStr
        return tmpStr


myBoard = Board()

#create pieces
w_rook_1 = Rook(1, myBoard, 'white', '11') #create a rook
# w_rook_2 = Rook(2, myBoard, 'white', '70') #create a rook
w_king = King(3, myBoard, 'white', '24') #create a king
# w_bishop_1 = Bishop(4, myBoard, 'white', '20')
# w_bishop_2 = Bishop(5, myBoard, 'white', '50')
# w_queen = Queen(6, myBoard, 'white', '30')
# w_pawn_1 = Pawn(1335, myBoard, 'white', '61')

# b_rook_1 = Rook(20, myBoard, 'black', '01')
b_king = King(21, myBoard, 'black', '71')
b_pawn_1 = Pawn(234, myBoard, 'black', '61')

#add them to the board
# myBoard.addPiece(w_rook_1) #add piece to board
# myBoard.addPiece(w_rook_2)
myBoard.addPiece(w_king)
myBoard.addPiece(w_rook_1)
# myBoard.addPiece(w_bishop_1)
# myBoard.addPiece(w_bishop_2)
# myBoard.addPiece(w_queen)
myBoard.addPiece(b_king)
myBoard.addPiece(b_pawn_1)
# myBoard.addPiece(b_pawn_1)






###-------GAME STARTS-------###
myGame = ChessGame(myBoard)
# myGame.runGame() should run the game


#whoever to move
moves = myGame.getPlayerMoves('black')
print(moves)






print(myBoard.toString())   #for å displaye brettet
print("\n")