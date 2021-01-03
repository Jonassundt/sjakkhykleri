"""King-piece"""


class King():
    def __init__(self, id, board, color, pos, name='♚'):
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
        
        moves = []

        #up
        tmpPos = str(x) + str(y + 1)
        tmpPiece = self.board.getPiece(tmpPos)
        if tmpPiece == None: #gone outside of the board
            pass #do nothing.
        elif(tmpPiece != 'o' and tmpPiece.color != self.color): #hvis det er en motstanderbrikke
            moves.append(self.pos + tmpPos)
        elif(tmpPiece == 'o'):
            moves.append(self.pos + tmpPos) #hvis det er et åpent felt, add.

        #upleft
        tmpPos = str(x - 1) + str(y + 1)
        tmpPiece = self.board.getPiece(tmpPos)
        if tmpPiece == None: #gone outside of the board
            pass #do nothing.
        elif(tmpPiece != 'o' and tmpPiece.color != self.color): #hvis det er en motstanderbrikke
            moves.append(self.pos + tmpPos)
        elif(tmpPiece == 'o'):
            moves.append(self.pos + tmpPos) #hvis det er et åpent felt, add.
        
        #left
        tmpPos = str(x - 1) + str(y)
        tmpPiece = self.board.getPiece(tmpPos)
        if tmpPiece == None: #gone outside of the board
            pass #do nothing.
        elif(tmpPiece != 'o' and tmpPiece.color != self.color): #hvis det er en motstanderbrikke
            moves.append(self.pos + tmpPos)
        elif(tmpPiece == 'o'):
            moves.append(self.pos + tmpPos) #hvis det er et åpent felt, add.
        
        #downleft
        tmpPos = str(x - 1) + str(y - 1)
        tmpPiece = self.board.getPiece(tmpPos)
        if tmpPiece == None: #gone outside of the board
            pass #do nothing.
        elif(tmpPiece != 'o' and tmpPiece.color != self.color): #hvis det er en motstanderbrikke
            moves.append(self.pos + tmpPos)
        elif(tmpPiece == 'o'):
            moves.append(self.pos + tmpPos) #hvis det er et åpent felt, add.
        
        #down
        tmpPos = str(x) + str(y - 1)
        tmpPiece = self.board.getPiece(tmpPos)
        if tmpPiece == None: #gone outside of the board
            pass #do nothing.
        elif(tmpPiece != 'o' and tmpPiece.color != self.color): #hvis det er en motstanderbrikke
            moves.append(self.pos + tmpPos)
        elif(tmpPiece == 'o'):
            moves.append(self.pos + tmpPos) #hvis det er et åpent felt, add.

        #downright
        tmpPos = str(x + 1) + str(y - 1)
        tmpPiece = self.board.getPiece(tmpPos)
        if tmpPiece == None: #gone outside of the board
            pass #do nothing.
        elif(tmpPiece != 'o' and tmpPiece.color != self.color): #hvis det er en motstanderbrikke
            moves.append(self.pos + tmpPos)
        elif(tmpPiece == 'o'):
            moves.append(self.pos + tmpPos) #hvis det er et åpent felt, add.

        #right
        tmpPos = str(x + 1) + str(y)
        tmpPiece = self.board.getPiece(tmpPos)
        if tmpPiece == None: #gone outside of the board
            pass #do nothing.
        elif(tmpPiece != 'o' and tmpPiece.color != self.color): #hvis det er en motstanderbrikke
            moves.append(self.pos + tmpPos)
        elif(tmpPiece == 'o'):
            moves.append(self.pos + tmpPos) #hvis det er et åpent felt, add.
        
        #upright
        tmpPos = str(x + 1) + str(y + 1)
        tmpPiece = self.board.getPiece(tmpPos)
        if tmpPiece == None: #gone outside of the board
            pass #do nothing.
        elif(tmpPiece != 'o' and tmpPiece.color != self.color): #hvis det er en motstanderbrikke
            moves.append(self.pos + tmpPos)
        elif(tmpPiece == 'o'):
            moves.append(self.pos + tmpPos) #hvis det er et åpent felt, add.

        return moves