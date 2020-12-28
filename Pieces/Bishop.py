"""Bishop-Piece"""


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
        
        #TODO: Add validity-check for if player is in check. Do this by trying to make each move, and checking if playerColor is in check,
        # If the player is in check, then dont add it to the moves. If it is not in check, then add that to the valid moves.
        # Do this by accessing the Game-class.
        return moves
