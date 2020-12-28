"""Just to visualize moves"""


myMoves = ['6757', '6756', '6777', '7666']
grid = [["o" for i in range(8)] for j in range(8)]



for move in myMoves:
    print(move[2:4])
    x = int(move[2:3])
    y = int(move[3:4])
    
    grid[y][x] = 'X'


tmpStr = ''
for y in grid:
    row = ''
    for elem in y:
        row += elem
    tmpStr = '\n' + row + tmpStr
print(tmpStr)
