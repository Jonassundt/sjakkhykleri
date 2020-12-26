import random
import copy

"""Chess-game"""

class ChessGame():

    def __init__(self, board):
        self.board = board
        self.kingPosBlack = '00' #sample positions
        self.kingPosWhite = '11'

    def runGame(self): #create this method later.
        pass

    def makeMove(self, move): #Only works when input is a move in the list of moves.
        #makes a move on the board and updates the pieces.
        startPos = move[0:2]
        endPos = move[2:4]
        startPiece = self.board.getPiece(startPos)
        # endPiece = self.board.getPiece(endPos)

        self.board.setPiece(startPiece, endPos)
        self.board.setPiece('o', startPos)
        pass

    def getPlayerMoves(self, playerColor, checkSelfCheck=1):
        #returns all possible moves on the board [XXXX, XXXY, XXXZ, ...]
        #goes for each piece in the game and adds moves to the list
        playerMoves = []
        resultMoves = []
        #går inn for hver brikke på brettet og samler trekk fra hver brikke.
        for x in range(8):
            for y in range(8):
                piece = self.board.getPiece(str(x) + str(y))
                if(piece != None and piece != 'o'): #sjekker at det er en brikke.
                    pieceMoves = piece.getMoves()
                    for move in pieceMoves:
                        playerMoves.append(move)
        #white make the move
        #isPlayerCheck(white)
        if(checkSelfCheck == 1):
            for move in playerMoves:
                self.makeMove(move) #makes the move
                blackMoves = self.getPlayerMoves('black', 0) #gets the possible other moves.
                if(self.isPlayerCheck('black') == False):
                    resultMoves.append(move)
                else:
                    pass
                #does undo of the move after it has been done.




        return playerMoves
    

    def isPlayerCheck(self, playerColor):
        #goes through opposite players moves and checks if any moves results in the kings position.
        if(playerColor == 'white'):
            for move in self.getPlayerMoves('black', 0):
                if move[2:4] == self.kingPosWhite:
                    return True
            return False
        
        #do same for black
        elif(playerColor == 'black'):
            for move in self.getPlayerMoves('white', 0):
                if move[2:4] == self.kingPosBlack:
                    return True
            return False

    def isCheckMate(self, playerColor):
        #if player has no moves left and it is his turn, then he is checkmate.
        if len(self.getPlayerMoves(playerColor) == 0):
            return True
        return False

class Board():
    """Only holds the board with the pieces"""
    def __init__(self):
        self.board = [["o" for i in range(8)] for j in range(8)]
    
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
    
    def setPiece(self, piece, pos): #sets a piece on a square position (might be Piece, or 'o')
        y = int(pos[1])
        x = int(pos[0])
        if(piece == 'o'):
            self.board[y][x] = 'o'
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

    


class Rook():
    """ id, color, name, board"""

    def __init__(self, id, board, color, pos, name='R'):
        self.id = id
        self.name = name #This shows on the board
        self.board = board
        self.pos = pos #ex '36'
        self.color = color
        print("Rook initialized.")

    def toString(self):
        return self.name
    
    def getMoves(self):
        x = int(self.pos[0])
        y = int(self.pos[1])

        moves = []
        #check above
        for i in range(1, 8 - y):
            tmpPos = str(x) + str(y + i)
            tmpPiece = self.board.getPiece(tmpPos)
            if tmpPiece == None: #gotten outside of the board.
                break
            #if pos is inside of the board.
            elif(tmpPiece != 'o' and tmpPiece.color != self.color): #hvis o, ok add kjør videre. hvis ikke o og den er annen farge, add til moves.
                moves.append(self.pos + tmpPos)
                break
            elif(tmpPiece == 'o'):
                moves.append(self.pos + tmpPos)
            elif(tmpPiece.color == self.color):
                break
        #check below
        for i in range(1, y + 1):
            tmpPos = str(x) + str(y - i)
            tmpPiece = self.board.getPiece(tmpPos)
            if tmpPiece == None: #gotten outside of the board.
                break
            #if pos is inside of the board.
            elif(tmpPiece != 'o' and tmpPiece.color != self.color): #hvis o, ok add kjør videre. hvis ikke o og den er annen farge, add til moves.
                moves.append(self.pos + tmpPos)
                break
            elif(tmpPiece == 'o'):
                moves.append(self.pos + tmpPos)
            elif(tmpPiece.color == self.color):
                break
        #check right
        for i in range(1, 8 - x):
            tmpPos = str(x + i) + str(y)
            tmpPiece = self.board.getPiece(tmpPos)
            if tmpPiece == None: #gotten outside of the board.
                break
            #if pos is inside of the board.
            elif(tmpPiece != 'o' and tmpPiece.color != self.color): #hvis o, ok add kjør videre. hvis ikke o og den er annen farge, add til moves.
                moves.append(self.pos + tmpPos)
                break
            elif(tmpPiece == 'o'):
                moves.append(self.pos + tmpPos)
            elif(tmpPiece.color == self.color):
                break
        #check left
        for i in range(1, x + 1):
            tmpPos = str(x - i) + str(y)
            tmpPiece = self.board.getPiece(tmpPos)
            if tmpPiece == None: #gotten outside of the board.
                break
            #if pos is inside of the board.
            elif(tmpPiece != 'o' and tmpPiece.color != self.color): #hvis o, ok add kjør videre. hvis ikke o og den er annen farge, add til moves.
                moves.append(self.pos + tmpPos)
                break
            elif(tmpPiece == 'o'):
                moves.append(self.pos + tmpPos)
            elif(tmpPiece.color == self.color):
                break
        return moves

class King():
    def __init__(self, id, board, color, pos, name='K'):
        self.id = id
        self.name = name #This shows on the board
        self.board = board
        self.pos = pos #ex '36'
        self.color = color
        print("King initialized.")

    def toString(self):
        return self.name

    def getMoves(self):
        x = int(self.pos[0])
        y = int(self.pos[1])
        print(x, y)
        moves = []

        #up
        if(self.board.getPiece(str(x) + str(y + 1)) == 'o'):
            moves.append(self.pos + str(x) + str(y + 1))
        #upleft
        if(self.board.getPiece(str(x - 1) + str(y + 1)) == 'o'):
            moves.append(self.pos + str(x - 1) + str(y + 1))
        #left
        if(self.board.getPiece(str(x - 1) + str(y)) == 'o'):
            moves.append(self.pos + str(x - 1) + str(y))
        #downleft
        if(self.board.getPiece(str(x - 1) + str(y - 1)) == 'o'):
            moves.append(self.pos + str(x - 1) + str(y - 1))
        #down
        if(self.board.getPiece(str(x) + str(y - 1)) == 'o'):
            moves.append(self.pos + str(x) + str(y - 1))
        #downright
        if(self.board.getPiece(str(x + 1) + str(y - 1)) == 'o'):
            moves.append(self.pos + str(x + 1) + str(y - 1))
        #right
        if(self.board.getPiece(str(x + 1) + str(y)) == 'o'):
            moves.append(self.pos + str(x + 1) + str(y))
        #upright
        if(self.board.getPiece(str(x + 1) + str(y + 1)) == 'o'):
            moves.append(self.pos + str(x + 1) + str(y + 1))
        return moves

class Queen():
    def __init__(self, id, board, color, pos, name='Q'):
        self.id = id
        self.name = name #This shows on the board
        self.board = board
        self.pos = pos #ex '36'
        self.color = color
        print("Queen initialized.")

    def toString(self):
        return self.name

    def getMoves(self):
        x = int(self.pos[0])
        y = int(self.pos[1])
        print(x, y)
        moves = []

        #taken from rook
        #check above
        for i in range(1, 8 - y):
            tmpPos = str(x) + str(y + i)
            tmpPiece = self.board.getPiece(tmpPos)
            if tmpPiece == None: #gotten outside of the board.
                break
            #if pos is inside of the board.
            elif(tmpPiece != 'o' and tmpPiece.color != self.color): #hvis o, ok add kjør videre. hvis ikke o og den er annen farge, add til moves.
                moves.append(self.pos + tmpPos)
                break
            elif(tmpPiece == 'o'):
                moves.append(self.pos + tmpPos)
            elif(tmpPiece.color == self.color):
                break
        #check below
        for i in range(1, y + 1):
            tmpPos = str(x) + str(y - i)
            tmpPiece = self.board.getPiece(tmpPos)
            if tmpPiece == None: #gotten outside of the board.
                break
            #if pos is inside of the board.
            elif(tmpPiece != 'o' and tmpPiece.color != self.color): #hvis o, ok add kjør videre. hvis ikke o og den er annen farge, add til moves.
                moves.append(self.pos + tmpPos)
                break
            elif(tmpPiece == 'o'):
                moves.append(self.pos + tmpPos)
            elif(tmpPiece.color == self.color):
                break
        #check right
        for i in range(1, 8 - x):
            tmpPos = str(x + i) + str(y)
            tmpPiece = self.board.getPiece(tmpPos)
            if tmpPiece == None: #gotten outside of the board.
                break
            #if pos is inside of the board.
            elif(tmpPiece != 'o' and tmpPiece.color != self.color): #hvis o, ok add kjør videre. hvis ikke o og den er annen farge, add til moves.
                moves.append(self.pos + tmpPos)
                break
            elif(tmpPiece == 'o'):
                moves.append(self.pos + tmpPos)
            elif(tmpPiece.color == self.color):
                break
            
        #check left
        for i in range(1, x + 1):
            tmpPos = str(x - i) + str(y)
            tmpPiece = self.board.getPiece(tmpPos)
            if tmpPiece == None: #gotten outside of the board.
                break
            #if pos is inside of the board.
            elif(tmpPiece != 'o' and tmpPiece.color != self.color): #hvis o, ok add kjør videre. hvis ikke o og den er annen farge, add til moves.
                moves.append(self.pos + tmpPos)
                break
            elif(tmpPiece == 'o'):
                moves.append(self.pos + tmpPos)
            elif(tmpPiece.color == self.color):
                break
        
        #taken from bishop
        #check up-right
        for i in range(1,8):
            tmpPos = str(x + i) + str(y + i)
            tmpPiece = self.board.getPiece(tmpPos)
            if tmpPiece == None: #is outside of board
                break
            #if pos is inside of the board
            elif(tmpPiece != 'o' and tmpPiece.color != self.color):
                moves.append(self.pos + tmpPos)
                break
            elif(tmpPiece == 'o'):
                moves.append(self.pos + tmpPos)
            elif(tmpPiece.color == self.color):
                break
        #check up-left
        for i in range(1,8):
            tmpPos = str(x - i) + str(y + i)
            tmpPiece = self.board.getPiece(tmpPos)
            if tmpPiece == None: #is outside of board
                break
            #if pos is inside of the board
            elif(tmpPiece != 'o' and tmpPiece.color != self.color):
                moves.append(self.pos + tmpPos)
                break
            elif(tmpPiece == 'o'):
                moves.append(self.pos + tmpPos)
            elif(tmpPiece.color == self.color):
                break
        #check down-left
        for i in range(1,8):
            tmpPos = str(x - i) + str(y - i)
            tmpPiece = self.board.getPiece(tmpPos)
            if tmpPiece == None: #is outside of board
                break
            #if pos is inside of the board
            elif(tmpPiece != 'o' and tmpPiece.color != self.color):
                moves.append(self.pos + tmpPos)
                break
            elif(tmpPiece == 'o'):
                moves.append(self.pos + tmpPos)
            elif(tmpPiece.color == self.color):
                break
        #check down-right
        for i in range(1,8):
            tmpPos = str(x + i) + str(y - i)
            tmpPiece = self.board.getPiece(tmpPos)
            if tmpPiece == None: #is outside of board
                break
            #if pos is inside of the board
            elif(tmpPiece != 'o' and tmpPiece.color != self.color):
                moves.append(self.pos + tmpPos)
                break
            elif(tmpPiece == 'o'):
                moves.append(self.pos + tmpPos)
            elif(tmpPiece.color == self.color):
                break

        return moves

class Bishop():
    """ id, color, name, board"""

    def __init__(self, id, board, color, pos, name='b'):
        self.id = id
        self.name = name #This shows on the board
        self.board = board
        self.pos = pos #ex '36'
        self.color = color
        print("Bishop initialized.")

    def toString(self):
        return self.name
    
    def getMoves(self):
        x = int(self.pos[0])
        y = int(self.pos[1])

        moves = []
        #check up-right
        for i in range(1,8):
            tmpPos = str(x + i) + str(y + i)
            tmpPiece = self.board.getPiece(tmpPos)
            if tmpPiece == None: #is outside of board
                break
            #if pos is inside of the board
            elif(tmpPiece != 'o' and tmpPiece.color != self.color):
                moves.append(self.pos + tmpPos)
                break
            elif(tmpPiece == 'o'):
                moves.append(self.pos + tmpPos)
            elif(tmpPiece.color == self.color):
                break
        #check up-left
        for i in range(1,8):
            tmpPos = str(x - i) + str(y + i)
            tmpPiece = self.board.getPiece(tmpPos)
            if tmpPiece == None: #is outside of board
                break
            #if pos is inside of the board
            elif(tmpPiece != 'o' and tmpPiece.color != self.color):
                moves.append(self.pos + tmpPos)
                break
            elif(tmpPiece == 'o'):
                moves.append(self.pos + tmpPos)
            elif(tmpPiece.color == self.color):
                break
        #check down-left
        for i in range(1,8):
            tmpPos = str(x - i) + str(y - i)
            tmpPiece = self.board.getPiece(tmpPos)
            if tmpPiece == None: #is outside of board
                break
            #if pos is inside of the board
            elif(tmpPiece != 'o' and tmpPiece.color != self.color):
                moves.append(self.pos + tmpPos)
                break
            elif(tmpPiece == 'o'):
                moves.append(self.pos + tmpPos)
            elif(tmpPiece.color == self.color):
                break
        #check down-right
        for i in range(1,8):
            tmpPos = str(x + i) + str(y - i)
            tmpPiece = self.board.getPiece(tmpPos)
            if tmpPiece == None: #is outside of board
                break
            #if pos is inside of the board
            elif(tmpPiece != 'o' and tmpPiece.color != self.color):
                moves.append(self.pos + tmpPos)
                break
            elif(tmpPiece == 'o'):
                moves.append(self.pos + tmpPos)
            elif(tmpPiece.color == self.color):
                break

        return moves


myBoard = Board()

#create pieces
w_rook_1 = Rook(1, myBoard, 'white', '70') #create a rook
w_rook_2 = Rook(2, myBoard, 'white', '00') #create a rook
w_king = King(3, myBoard, 'white', '40') #create a king
w_bishop_1 = Bishop(4, myBoard, 'white', '20')
w_bishop_2 = Bishop(5, myBoard, 'white', '50')
w_queen = Queen(6, myBoard, 'white', '30')

b_rook_1 = Rook(20, myBoard, 'black', '76')
b_king = King(21, myBoard, 'white', '77')

#add them to the board
myBoard.addPiece(w_rook_1) #add piece to board
myBoard.addPiece(w_rook_2)
myBoard.addPiece(w_king)
myBoard.addPiece(w_bishop_1)
myBoard.addPiece(w_bishop_2)
myBoard.addPiece(w_queen)
myBoard.addPiece(b_rook_1)
myBoard.addPiece(b_king)


print(myBoard.toString())   #for å displaye brettet
# print(myBoard.getPiece('53')) #for å få tak i en brikke

# print(myBoard.getPiece('62').getMoves()) => ['XXXX', 'XXXY', 'XXXZ']

# print(myBoard.getPiece('53').getMoves())
# print(myBoard.getPiece('53').getMoves())
# print(myBoard.getPiece('33').getMoves())

###-------GAME STARTS-------###
myGame = ChessGame(myBoard)

#white to choose a move
moves = myGame.getPlayerMoves('white')
print(moves)
#want to move my a1 rook to a2
myGame.makeMove('0010')

#display board again
print(myBoard.toString())

#blacks turn
moves = myGame.getPlayerMoves('black')
print(moves)



