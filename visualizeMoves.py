"""Just to visualize moves"""


myMoves = ['0102', '0103', '0104', '0105', '0106', '0107', '0100', '0111', '0121', '0131', '0141', '0151', '0161', '0171', '4243', '4233', '4232', '4251', '4252', '4253', '7675', '7674']
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
