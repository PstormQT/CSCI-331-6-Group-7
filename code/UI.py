import tkinter as tk
import model  # make sure model.py is in the same folder

class UI:
    def __init__(self):
        self.model = model.Board2048()
        self.root = tk.Tk()
        self.root.title("2048 with AI")
        self.currBoardUI = []
        self.currentScore = None

        
    def start(self,mode: int):
        self.model = model.Board2048()
        for widget in self.root.winfo_children():
            widget.destroy()
        self.currBoardUI = []

        if mode == 1:
            self.renderMode()
            self.renderBoard()
            self.movementButtons()

        self.root.mainloop()

    def renderMode(self):
        mode = tk.Frame(self.root)
        mode.grid(row = 0, column = 0, columnspan = 5)

        reset = tk.Button(mode, height=5, width=20, text="reset", command = lambda : self.start(1))
        reset.grid(row=0, column=1, padx=5, pady=5)

        AImode1 = tk.Button(mode, height=5, width=20, text="AI Mode 1, TBD")
        AImode1.grid(row=0, column=2, padx=5, pady=5)

        AImode2 = tk.Button(mode, height=5, width=20, text="AI Mode 2, TBD")
        AImode2.grid(row=0, column=3, padx=5, pady=5)

        self.currentScore = tk.Label(mode, height = 5, width = 20, text = f"Current Score: {self.model.getScore()}")
        self.currentScore.grid(row = 0, column = 0,  padx=5, pady=5)
        

    def renderBoard(self):
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
        self.model.playAction(direction)
        self.updateBoard()
        if self.model.getGameOver():
            self.currentScore.config(text = f"GAME OVER, Score: {self.model.getScore()}")
        else:
            self.updateScore()    

    def updateScore(self):
        self.currentScore.config(text = f"Current Score: {self.model.getScore()}")

    def updateBoard(self):
        board = self.model.getBoard()
        for i in range(4):
            for j in range(4):
                value = board[i][j]
                text = str(value) if value != 0 else ""
                uiboard = self.currBoardUI[i][j]
                uiboard.config(text=text, bg=self.get_color(value))

    def get_color(self, value):
        """Return a background color based on the tile value."""
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
            2048: "#edc22e"
        }
        return colors.get(value, "#3c3a32")


if __name__ == "__main__":
    a = UI()
    a.start(1)