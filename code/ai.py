import model
import copy

inf = 2**64
perfect_snake = [[2, 2**2, 2**3, 2**4],
                 [2**8, 2**7, 2**6, 2**5],
                 [2**9, 2**10, 2**11, 2**12],
                 [2**16, 2**15, 2**14, 2**13],]

def snakeHeuristic(board):
    h = 0
    for i in range(board.MAX_BOARD_DIMENSION):
        for j in range(board.MAX_BOARD_DIMENSION):
            h += board[i][j] * perfect_snake[i][j]
    return h

def getNextMove(board):
    depth = 2
    bestScore = -inf
    nextBestMove = model.Direction[0]
    # results = []

    for dir in model.directions:
        simBoard = copy.deepcopy(board)
        score, validMove = simBoard.move(dir, False)
        if not validMove:
            continue
        score, move = expectiminimax(simBoard, depth, dir)
        if score > bestScore:
            bestScore = score
            nextBestMove = dir

    return nextBestMove

def expectiminimax(board, depth, dir = None):
    if board.getGameOver():
        return -inf, dir
    elif depth < 0:
        return snakeHeuristic(board), dir
    
    a = 0
    if depth != int(depth):
        #Player's turn, max
        a = -inf
        for dir in model.Direction:
            simBoard = copy.deepcopy(board)
            score, moved = simBoard.move(dir, False)
            if moved:
                res = expectiminimax(simBoard, depth-0.5, dir)[0]
                if res > a:a = res
    elif depth == int(depth):
        #Nature's turn, calc the average
        a = 0
        openTiles = board.getAllOpenCells()
        for addTileLoc in openTiles:
            board.addTile(addTileLoc, 2)
            a += 1.0/len(openTiles)*expectiminimax(board, depth - 0.5, dir)[0]
            board.addTile(addTileLoc, 0)
    return (a, dir)
        