import tkinter as tk
import model
import expectiminimax as emm
import montecarlo as mc

class UI:
    SEARCH_DEPTH = 4
    MONTE_CARLO_SIMULATION_COUNT = 100
    MONTE_CARLO_SIMULATION_DEPTH = 100

    def __init__(self):
        self.model = model.Board2048()
        self.root = tk.Tk()
        self.root.title("2048 with AI")
        self.currBoardUI = []
        self.currentScore = None
        
    def start(self,mode: int):
        """
        The starter for the game, init all of the component depend on the 5mode

        Args:
            mode (int): What mode to run... 1: Manual, 2: ExpectiMinimax, 3: Monte Carlo 
        """
        self.model = model.Board2048()
        for widget in self.root.winfo_children():
            widget.destroy()
        self.currBoardUI = []

        # Manual Mode
        if mode == 1:
            self.renderMode()
            self.renderBoard()
            self.movementButtons()

        elif mode == 2:
            self.renderMode()
            self.renderBoard()
            self.runMiniMax()

        elif mode == 3:
            self.renderMode()
            self.renderBoard()
            self.runMonteCarlo()
        
        self.root.mainloop()


    def runMonteCarlo(self):
        """
        Run the Monte Carlo tree search
        """
        if self.model.getGameOver():
            self.currentScore.config(text=f"GAME OVER, Score: {self.model.getScore()}")
            return

        # Search Monte carlo tree search with 100 simulation with 100 depth
        nextMove = mc.getBestMove(self.model, self.MONTE_CARLO_SIMULATION_COUNT, self.MONTE_CARLO_SIMULATION_DEPTH)
        self.movementFunction(nextMove)

        # Running at max speed (timing out at 10ms)
        self.root.after(10, self.runMonteCarlo)

    def runMiniMax(self):
        """
        Run the Minimax Simulation 
        """
        if self.model.getGameOver():
            self.currentScore.config(text=f"GAME OVER, Score: {self.model.getScore()}")
            return

        # Search Tree depth of 3
        nextMove = emm.getNextMove(self.model, self.SEARCH_DEPTH)
        self.movementFunction(nextMove)

        # Running at max speed (timing out at 10ms)
        self.root.after(10, self.runMiniMax)

    def renderMode(self):
        """
        Spawning all of the input buttons for the game
        """
        mode = tk.Frame(self.root)
        mode.grid(row = 0, column = 0, columnspan = 5)

        reset = tk.Button(mode, height=5, width=20, text="Manual Playing", command = lambda : self.start(1))
        reset.grid(row=0, column=1, padx=5, pady=5)

        AImode1 = tk.Button(mode, height=5, width=20, text="AI Mode 1\nExpectiminimax", command = lambda : self.start(2))
        AImode1.grid(row=0, column=2, padx=5, pady=5)

        AImode2 = tk.Button(mode, height=5, width=20, text="AI Mode 2\nMonte Carlo Search Tree", command = lambda : self.start(3))
        AImode2.grid(row=0, column=3, padx=5, pady=5)

        self.currentScore = tk.Label(mode, height = 5, width = 20, text = f"Current Score: {self.model.getScore()}")
        self.currentScore.grid(row = 0, column = 0,  padx=5, pady=5)
        

    def renderBoard(self):
        """
        Render the board itself
        """
        board = self.model.getBoard()
        frame = tk.Frame(self.root, bg = "#000000")
        frame.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        for i in range(4):
            holder = []
            for j in range(4):
                value = board[i][j]
                text = str(value) if value != 0 else ""
                cell = tk.Label(
                    frame,
                    text=text,
                    width=8,
                    height=4,
                    font=("Helvetica", 20, "bold"),
                    bg=self.get_color(value),
                    fg="black"
                )
                cell.grid(row=i, column=j, padx=5, pady=5)
                holder.append(cell)
            self.currBoardUI.append(holder)

    def movementButtons(self):
        """
        Render the button for manual mode
        """
        buttonFrame = tk.Frame(self.root, bg = "#4287f5", padx= 20, pady = 20)
        buttonFrame.grid(row = 1, column = 4)

        buttonUp = tk.Button(buttonFrame, text = "↑",width=4,height=2,font=("Helvetica", 20, "bold"), command = lambda : self.movementFunction(1))
        buttonUp.grid(row = 0, column = 1)

        buttonDown = tk.Button(buttonFrame, text = "↓", command = lambda : self.movementFunction(2),width=4,height=2,font=("Helvetica", 20, "bold"))
        buttonDown.grid(row = 2, column = 1)

        buttonLeft = tk.Button(buttonFrame, text = "←", command = lambda : self.movementFunction(3),width=4,height=2,font=("Helvetica", 20, "bold"))
        buttonLeft.grid(row = 1, column = 0)

        buttonRight = tk.Button(buttonFrame, text = "→", command = lambda : self.movementFunction(4),width=4,height=2,font=("Helvetica", 20, "bold"))
        buttonRight.grid(row = 1, column = 2)

    def movementFunction(self, direction: int):
        """
        Trigger the movement for the board

        Args:
            direction (int): input for the movement... 1: Up, 2: Down, 3: Left, 4: Right
        """
        self.model.playAction(direction)
        self.updateBoard()
        if self.model.getGameOver():
            self.currentScore.config(text = f"GAME OVER, Score: {self.model.getScore()}")
        else:
            self.updateScore()    

    def updateScore(self):
        """
        Update the score for the UI
        """
        self.currentScore.config(text = f"Current Score: {self.model.getScore()}")

    def updateBoard(self):
        """
        Update the board for the UI
        """
        board = self.model.getBoard()
        for i in range(4):
            for j in range(4):
                value = board[i][j]
                text = str(value) if value != 0 else ""
                uiboard = self.currBoardUI[i][j]
                uiboard.config(text=text, bg=self.get_color(value))

    def get_color(self, value: int) -> str:
        """
        Getting the color value for the number

        Args:
            value (int): the integer to get the value

        Returns:
            str: the color
        """
        colors = {
            0: "#cdc1b4",
            2: "#eee4da",
            4: "#ede0c8",
            8: "#f2b179",
            16: "#f59563",
            32: "#f67c5f",
            64: "#f65e3b",
            128: "#edcf72",
            256: "#edcc61",
            512: "#edc850",
            1024: "#edc53f",
            2048: "#edc22e",
            4096: "#66d56c",
            8192: "#24C8B5",
            16384: "#1D72C1",
            32768: "#7050d2"
        }
        return colors.get(value, "#3c3a32")

if __name__ == "__main__":
    a = UI()
    a.start(1)
