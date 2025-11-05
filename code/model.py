from enum import Enum
import copy, random

class Direction(Enum):
    """
    Class to represent the 4 directions of movement.\n
    UP = 1, DOWN = 2, LEFT = 3, RIGHT = 4.
    """
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

class Board2048:
    """
    Class to represent the board of the 2048 game.\n
    Board coordinates are represented as (y, x)
    """
    MAX_BOARD_DIMENSION = 4
    TILE_2_CHANCE = 0.9
    TILE_4_CHANCE = 0.1

    def __init__(self):
        self.board = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        self.score = 0
        self.game_over = False
        self.addTile()
        self.addTile()

    def getAllOpenCells(self):
        """
        This returns a list of all open cells in the game board.
        """
        open_cells = []
        for y in range(self.MAX_BOARD_DIMENSION):
            for x in range(self.MAX_BOARD_DIMENSION):
                if self.board[y][x] == 0:
                    open_cells.append((y, x))
        return open_cells

    def addTile(self):
        """
        This adds a random tile to the board.
        """
        open_cells = self.getAllOpenCells()
        if open_cells != []:
            y, x = random.choice(open_cells)
            cell_num_prob = random.random()
            if cell_num_prob < self.TILE_2_CHANCE:
                self.board[y][x] = 2
            else:
                self.board[y][x] = 4

    def merge(self, list_values: list):
        """
        This merges and combines numbers from right to right for a single row/column.\n
        It start are the right and merges values in the right direction.\n
        Row - [Left, Right], Col - [Bottom, Top]

        Args:
            list_values (list): The row/column list of values to combine

        Returns:
            list: The updated row/column list of values after the shift/merge.
        """
        list_values = [v for v in list_values if v != 0]
        final_values = []
        i = len(list_values) - 1
        while i >= 0:
            if i - 1 >= 0 and list_values[i] == list_values[i - 1]:
                final_values.append(list_values[i] * 2)
                self.score += list_values[i] * 2
                i -= 2
            else:
                final_values.append(list_values[i])
                i -= 1

        while len(final_values) < 4:
            final_values.append(0)
        final_values.reverse()
        return final_values

    def move(self, direction) -> bool:
        """
        This moves the tiles on the board in the desired direction.

        Args:
            direction (int): The direction to move all of the tiles.

        Returns:
            bool: If the board changed after trying to move the pieces.
        """
        if self.game_over:
            print(f"The game is over. Your prior score was {self.score}. You cannot move anymore.")
            return False

        original_board = copy.deepcopy(self.board)

        if direction == Direction.UP.value:
            for col in range(self.MAX_BOARD_DIMENSION):
                initial_values = [self.board[row][col] for row in range(self.MAX_BOARD_DIMENSION - 1, -1, -1)]
                final_values = self.merge(initial_values)
                for row in range(self.MAX_BOARD_DIMENSION):
                    self.board[row][col] = final_values[3 - row]
        elif direction == Direction.DOWN.value:
            for col in range(self.MAX_BOARD_DIMENSION):
                initial_values = [self.board[row][col] for row in range(self.MAX_BOARD_DIMENSION)]
                final_values = self.merge(initial_values)
                for row in range(self.MAX_BOARD_DIMENSION):
                    self.board[row][col] = final_values[row]
        elif direction == Direction.LEFT.value:
            for row in range(self.MAX_BOARD_DIMENSION):
                initial_values = [self.board[row][col] for col in range(self.MAX_BOARD_DIMENSION - 1, -1, -1)]
                final_values = self.merge(initial_values)
                for col in range(self.MAX_BOARD_DIMENSION):
                    self.board[row][col] = final_values[3 - col]
        elif direction == Direction.RIGHT.value:
            for row in range(self.MAX_BOARD_DIMENSION):
                initial_values = [self.board[row][col] for col in range(self.MAX_BOARD_DIMENSION)]
                final_values = self.merge(initial_values)
                for col in range(self.MAX_BOARD_DIMENSION):
                    self.board[row][col] = final_values[col]

        return original_board != self.board

    def updateGameOver(self) -> bool:
        """
        This checks if there are no more moves to be made on the game board.
        Returns:
            bool: True if game is over, False is there are still moves to be made.
        """
        for row in range(self.MAX_BOARD_DIMENSION):
            for col in range(self.MAX_BOARD_DIMENSION):
                if (self.board[row][col] == 0):
                    self.game_over = False
                    return
                
        for i in range(self.MAX_BOARD_DIMENSION):
            for j in range(self.MAX_BOARD_DIMENSION - 1):
                if (self.board[j][i] == self.board[j+1][i] or self.board[i][j] == self.board[i][j+1]):
                    self.game_over = False
                    return

        self.game_over = True

    def setBoard(self, board: list):
        self.board = board

    def getBoard(self) -> list:
        return self.board

    def getScore(self) -> int:
        return self.score
    
    def getGameOver(self) -> bool:
        return self.game_over

    def displayCLI(self):
        """
        This displays the current CLI board and score.
        """
        print("----------------------------------------")
        print(f"Score: {self.score}")
        for i in range(self.MAX_BOARD_DIMENSION):
            for j in range(self.MAX_BOARD_DIMENSION):
                print(f"{self.board[i][j]}  ", end='')
            print(" ")

    def playAction(self, direction):
        """
        This moves the tiles in a given direction, adds a new tile, and checks if the game is over.
        Args:
            direction (int): The direction to move all of the tiles.
        """
        changed = self.move(direction)
        if (changed):
            self.addTile()
            self.updateGameOver()
    
    def playActionCLI(self, direction):
        """
        This moves the tiles in a given direction, adds a new tile, and checks if the game is over.\n
        This also displays the current CLI board and score. 
        Args:
            direction (int): The direction to move all of the tiles.
        """
        changed = self.move(direction)
        if (changed):
            self.addTile()
            self.updateGameOver()
        self.displayCLI()

def main():
    print("Starting 2048")
    game = Board2048()
    game.displayCLI()
    while (not game.game_over):
        direction = input("Give a direction using WASD: North is 'W', South is 'S', Left is 'A', Right is 'D': ")
        direction = direction.lower()
        match direction:
            case "w":
                game.playActionCLI(1)
            case "s":
                game.playActionCLI(2)
            case "a":
                game.playActionCLI(3)
            case "d":
                game.playActionCLI(4)
    print("Game Over")
    print(f"Final Score: {game.score}")

if __name__ == '__main__':
    main()
