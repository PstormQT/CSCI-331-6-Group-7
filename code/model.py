



class model2048:
    board = None
    score = 0
    state = True

    # Board 4x4 board itself
    # score = init to 0
    # state (still playing or dead) = True if still playing, False if it is not
    def __init__(self):
        self.board = [[0,2,4,8],[16,32,64,128],[256,512,1024,2048],[0,0,0,0]]
        self.score = 0

    def getScore(self) -> int:
        pass

    def getBoard(self) -> list:
        return self.board
    
    # Add a movement to the board. 
    # 1 for up
    # 2 for down
    # 3 for left
    # 4 for right
    def moveBoard(move: int):
        pass