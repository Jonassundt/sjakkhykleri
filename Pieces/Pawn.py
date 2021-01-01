"""Pawn-piece"""


class Pawn():
    """ id, color, name, board"""

    def __init__(self, id, board, color, pos, name='b'):
        self.id = id
        self.name = name #This shows on the board
        self.board = board
        self.pos = pos #ex '36'
        self.color = color
        print("Pawn initialized.")

    def toString(self):
        return self.name
    
    def getWhiteMoves(self):
        x = int(self.pos[0])
        y = int(self.pos[1])
        moves = []

        #check 1 up
        tmpPos = str(x) + str(y + 1)
        tmpPiece = self.board.getPiece(tmpPos)
        if(tmpPiece == None): #is outside of board
            pass
        #if pos is inside of the board
        elif(tmpPiece == 'o'): #open square ahead
            moves.append(self.pos + tmpPos)
            #if it is at startposition, check 2 up. This will only be checked if 1 up is a clear square.
            if(y == 1):
                tmpPos = str(x) + str(y + 2)
                tmpPiece = self.board.getPiece(tmpPos)
                if(tmpPiece == None): #it will never reach this. TODO: Can remove this.
                    pass
                elif(tmpPiece == 'o'):
                    moves.append(self.pos + tmpPos)
        
        #checks up-right
        tmpPos = str(x + 1) + str(y + 1)
        tmpPiece = self.board.getPiece(tmpPos)
        if(tmpPiece == None): #is outside of board
            pass
        #if pos is inside of board
        elif(tmpPiece != 'o' and tmpPiece.color != self.color): #if it is an opponents piece, ok
            moves.append(self.pos + tmpPos)
        #note here that we dont add to moves if it is not opponents piece, because pawns can only take diagonally.

        #checks up-left
        tmpPos = str(x - 1) + str(y + 1)
        tmpPiece = self.board.getPiece(tmpPos)
        if(tmpPiece == None): #is outside of board
            pass
        #if position is inside of board
        elif(tmpPiece != 'o' and tmpPiece.color != self.color): #opponents piece, ok
            moves.append(self.pos + tmpPos)
        
        return moves

    def getBlackMoves(self):
        x = int(self.pos[0])
        y = int(self.pos[1])
        moves = []

        #check 1 down
        tmpPos = str(x) + str(y - 1)
        tmpPiece = self.board.getPiece(tmpPos)
        if(tmpPiece == None): #is outside of board
            pass
        #if pos is inside of the board
        elif(tmpPiece == 'o'): #open square ahead
            moves.append(self.pos + tmpPos)
            #if it is at startposition, check 2 up. This will only be checked if 1 up is a clear square.
            if(y == 1):
                tmpPos = str(x) + str(y - 2)
                tmpPiece = self.board.getPiece(tmpPos)
                if(tmpPiece == None): #it will never reach this. TODO: Can remove this.
                    pass
                elif(tmpPiece == 'o'):
                    moves.append(self.pos + tmpPos)
        
        #checks down-right
        tmpPos = str(x + 1) + str(y - 1)
        tmpPiece = self.board.getPiece(tmpPos)
        if(tmpPiece == None): #is outside of board
            pass
        #if pos is inside of board
        elif(tmpPiece != 'o' and tmpPiece.color != self.color): #if it is an opponents piece, ok
            moves.append(self.pos + tmpPos)
        #note here that we dont add to moves if it is not opponents piece, because pawns can only take diagonally.

        #checks down-left
        tmpPos = str(x - 1) + str(y - 1)
        tmpPiece = self.board.getPiece(tmpPos)
        if(tmpPiece == None): #is outside of board
            pass
        #if position is inside of board
        elif(tmpPiece != 'o' and tmpPiece.color != self.color): #opponents piece, ok
            moves.append(self.pos + tmpPos)
        
        return moves

    def getMoves(self):
        if(self.color == 'white'):
            return self.getWhiteMoves()
        elif(self.color == 'black'):
            return self.getBlackMoves()
        else:
            print("something went wrong in getMoves() for pawn id " + str(self.id))
        


"""
TODO:
- make code more clear
- solve for queening (when it is reaching the opposite point of the board, turning into a queen)
"""