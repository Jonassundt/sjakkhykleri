"""Knight-Piece"""

"""
TODO: Really ugly code, clean it up.
"""

class Knight():
    """ id, color, name, board"""

    def __init__(self, id, board, color, pos, name='♞'):
        self.id = id
        self.name = name #This shows on the board
        self.board = board
        self.pos = pos #ex '36'
        self.color = color
        print("Knight initialized.")

    def toString(self):
        return self.name
    
    def getMoves(self):
        x = int(self.pos[0])
        y = int(self.pos[1])

        moves = []
        #check 1 right 2 up (up-right)
        tmpPos = str(x + 1) + str(y + 2)
        tmpPiece = self.board.getPiece(tmpPos)
        if tmpPiece == None: #is outside of board
            pass
        #if pos is inside of the board
        elif(tmpPiece != 'o' and tmpPiece.color != self.color):
            moves.append(self.pos + tmpPos)
        elif(tmpPiece == 'o'):
            moves.append(self.pos + tmpPos)
        
        #check 1 left 2 up (up-right)
        tmpPos = str(x - 1) + str(y + 2)
        tmpPiece = self.board.getPiece(tmpPos)
        if tmpPiece == None: #is outside of board
            pass
        #if pos is inside of the board
        elif(tmpPiece != 'o' and tmpPiece.color != self.color):
            moves.append(self.pos + tmpPos)
        elif(tmpPiece == 'o'):
            moves.append(self.pos + tmpPos)
        
        #check 2 left 1 up
        tmpPos = str(x - 2) + str(y + 1)
        tmpPiece = self.board.getPiece(tmpPos)
        if tmpPiece == None: #is outside of board
            pass
        #if pos is inside of the board
        elif(tmpPiece != 'o' and tmpPiece.color != self.color):
            moves.append(self.pos + tmpPos)
        elif(tmpPiece == 'o'):
            moves.append(self.pos + tmpPos)
        
        #check 2 left 1 down 
        tmpPos = str(x - 2) + str(y - 1)
        tmpPiece = self.board.getPiece(tmpPos)
        if tmpPiece == None: #is outside of board
            pass
        #if pos is inside of the board
        elif(tmpPiece != 'o' and tmpPiece.color != self.color):
            moves.append(self.pos + tmpPos)
        elif(tmpPiece == 'o'):
            moves.append(self.pos + tmpPos)

        #check 1 left 2 down
        tmpPos = str(x - 1) + str(y - 2)
        tmpPiece = self.board.getPiece(tmpPos)
        if tmpPiece == None: #is outside of board
            pass
        #if pos is inside of the board
        elif(tmpPiece != 'o' and tmpPiece.color != self.color):
            moves.append(self.pos + tmpPos)
        elif(tmpPiece == 'o'):
            moves.append(self.pos + tmpPos)

        #check 1 right 2 down
        tmpPos = str(x + 1) + str(y - 2)
        tmpPiece = self.board.getPiece(tmpPos)
        if tmpPiece == None: #is outside of board
            pass
        #if pos is inside of the board
        elif(tmpPiece != 'o' and tmpPiece.color != self.color):
            moves.append(self.pos + tmpPos)
        elif(tmpPiece == 'o'):
            moves.append(self.pos + tmpPos)
        
        #check 2 right 1 down
        tmpPos = str(x + 2) + str(y - 1)
        tmpPiece = self.board.getPiece(tmpPos)
        if tmpPiece == None: #is outside of board
            pass
        #if pos is inside of the board
        elif(tmpPiece != 'o' and tmpPiece.color != self.color):
            moves.append(self.pos + tmpPos)
        elif(tmpPiece == 'o'):
            moves.append(self.pos + tmpPos)
        
        #check 2 right 1 up
        tmpPos = str(x + 2) + str(y + 1)
        tmpPiece = self.board.getPiece(tmpPos)
        if tmpPiece == None: #is outside of board
            pass
        #if pos is inside of the board
        elif(tmpPiece != 'o' and tmpPiece.color != self.color):
            moves.append(self.pos + tmpPos)
        elif(tmpPiece == 'o'):
            moves.append(self.pos + tmpPos)

        return moves
