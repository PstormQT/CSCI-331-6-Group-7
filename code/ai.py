import copy
import model

INF = float("inf")

# Init block placement used to calculate the heurisitic
PERFECT_SNAKE = [
    [2**15, 2**14, 2**13, 2**12],
    [2**8,  2**9,  2**10, 2**11],
    [2**7,  2**6,  2**5,  2**4],
    [2**0,  2**1,  2**2,  2**3]
]


def getHeurisiticScore(board) -> int:
    """
    summary_ Scoring function of how the current board from the perfect game

    Args:
        board_obj (Board2048): The board for 2048

    Returns:
        int: Score value on how identical of the current board to the perfect board
    """
    board_heurisitic = 0
    grid = board.getBoard()
    size = board.MAX_BOARD_DIMENSION
    for i in range(size):
        for j in range(size):
            board_heurisitic += grid[i][j] * PERFECT_SNAKE[i][j]
    return board_heurisitic 

def getNextMove(board, depth):
    """
    _summary_: runner to get the best move from the board

    Args:
        board_obj (Board2048): The board itself
        depth (int): Depth of the search tree for expectiminimax

    Returns:
        int: direction to take 1: Up, 2: Down, 3: Left, 4: Right
    """
    bestScore = -INF
    bestMove = model.Direction.UP.value  # default

    # Spawning next move for all direction
    for dirEnum in model.Direction:
        dirVal = dirEnum.value
        simBoard = copy.deepcopy(board)
        moved = simBoard.move(dirVal)
        if not moved:
            continue

        # Player's turn for each potenial input
        score = expectiminimax(simBoard, depth - 1, False)
        if score > bestScore:
            bestScore = score
            bestMove = dirVal

    return bestMove


def expectiminimax(board, depth, playerTurn):
    """
    _summary_: Runner for the expectiminimax function for 2048 

    Args:
        board_obj (Board2048): The board object itself
        depth (int): the current depth
        playerTurn (_type_): Is it player turn

    Returns:
        int: the max score for that function
    """

    # Check if game over or depth = 0
    if board.getGameOver() or depth <= 0:
        return getHeurisiticScore(board)

    # Run max for player
    if playerTurn:
        maxScore = -INF
        moveCheck = False
        
        # Move simulation for each direction
        for dirEnum in model.Direction:
            dirVal = dirEnum.value
            sim = copy.deepcopy(board)
            moved = sim.move(dirVal)
            if not moved:
                continue
            moveCheck = True
            score = expectiminimax(sim, depth - 1, False)
            if score > maxScore:
                maxScore = score

        # Check if all future states are dead -> return raw score
        if not moveCheck:
            return getHeurisiticScore(board)
        return maxScore

    else:
        # Running for min node, spawning 2 or 4 tile in all possible location and return their average
        openCells = board.getAllOpenCells()
        if not openCells:
            return getHeurisiticScore(board)

        total_expected = 0.0
        p2 = 0.9
        p4 = 0.1

        # Running though all possible combination
        for (y, x) in openCells:
            sim2 = copy.deepcopy(board)
            sim2.board[y][x] = 2
            val2 = expectiminimax(sim2, depth - 1, True)

            sim4 = copy.deepcopy(board)
            sim4.board[y][x] = 4
            val4 = expectiminimax(sim4, depth - 1, True)

            total_expected += (p2 * val2 + p4 * val4)

        # average across open cells
        return total_expected / len(openCells)
