from enum import Enum
import random

class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

"""
Class to represent the board of the 2048 game.
Board coordinates are represented as (y, x)
"""
class Board2048:
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
        open_cells = []
        for y in range(self.MAX_BOARD_DIMENSION):
            for x in range(self.MAX_BOARD_DIMENSION):
                if self.board[y][x] == 0:
                    open_cells.append((y, x))
        return open_cells

    def addTile(self):
        open_cells = self.getAllOpenCells()
        if open_cells == []:
            print("Game Over")
            print(f"Final Score: {self.score}")
            self.game_over = True
        else:
            y, x = random.choice(open_cells)
            cell_num_prob = random.random()
            if cell_num_prob < self.TILE_2_CHANCE:
                self.board[y][x] = 2
            else:
                self.board[y][x] = 4
    


    """
    def merge(self, row, col, delta) -> int:
        points = 0
        for i in range(self.MAX_BOARD_DIMENSION):
            cor = None
            while()
        return points"""

    def merge(self, list_values):
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

    def move(self, direction):
        if self.game_over:
            print(f"The game is over. Your prior score was {self.score}. You cannot move anymore.")
            print("Call reset() to start again.")
            return
        
        """movement = None
        match direction:
            case Direction.UP:
                movement = (1, 0)
            case Direction.Down:
                movement = (-1, 0)
            case Direction.LEFT:
                movement = (0, -1)
            case Direction.RIGHT:
                movement = (0, 1)"""
        
        if direction == Direction.UP:
            for i in range(self.MAX_BOARD_DIMENSION):
                initial_values = []
                for j in range(self.MAX_BOARD_DIMENSION - 1, -1, -1):
                    initial_values.append(self.board[j][i])
                final_values = self.merge(initial_values)
                l = 0
                for j in range(self.MAX_BOARD_DIMENSION - 1, -1, -1):
                    self.board[j][i] = final_values[l]
                    l += 1
        elif direction == Direction.DOWN:
            for i in range(self.MAX_BOARD_DIMENSION):
                initial_values = []
                for j in range (0, self.MAX_BOARD_DIMENSION, 1):
                    initial_values.append(self.board[j][i])
                final_values = self.merge(initial_values)
                l = 0
                for j in range (0, self.MAX_BOARD_DIMENSION, 1):
                    self.board[j][i] = final_values[l]
                    l += 1
        elif direction == Direction.LEFT:
            for i in range(self.MAX_BOARD_DIMENSION):
                initial_values = []
                for j in range(self.MAX_BOARD_DIMENSION - 1, -1, -1): 
                    initial_values.append(self.board[i][j])
                final_values = self.merge(initial_values)
                l = 0
                for j in range(self.MAX_BOARD_DIMENSION - 1, -1, -1): 
                    self.board[j][i] = final_values[l]
                    l += 1
        elif direction == Direction.RIGHT:
            for i in range(self.MAX_BOARD_DIMENSION):
                initial_values = []
                for j in range(0, self.MAX_BOARD_DIMENSION, 1):
                    initial_values.append(self.board[i][j])
                final_values = self.merge(initial_values)
                l = 0
                for j in range(0, self.MAX_BOARD_DIMENSION, 1):
                    self.board[j][i] = final_values[l]
                    l += 1
    
    def reset(self):
        self.board = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        self.score = 0
        self.game_over = False
        self.addTile()
        self.addTile()

    def getScore(self) -> int:
        return self.score
    
    def getBoard(self) -> list:
        return self.board

    def display(self):
        for i in range(self.MAX_BOARD_DIMENSION):
            for j in range(self.MAX_BOARD_DIMENSION):
                print(f"{self.board[i][j]}  ", end='')
            print(" ")

def main():
    print("Starting 2048")
    game = Board2048()
    game.display()
    while (not game.game_over):
        direction = input("Give us a direction: North is W, South is S, Left is A, Right is D: ")
        direction = direction.lower()
        match direction:
            case "w":
                game.move(1)
                game.display()
            case "s":
                game.move(2)
                game.display()
            case "a":
                game.move(3)
                game.display()
            case "d":
                game.move(4)
                game.display()

if __name__ == '__main__':
    main()
