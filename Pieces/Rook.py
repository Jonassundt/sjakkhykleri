
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
