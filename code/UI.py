import tkinter as tk
import model  # make sure model.py is in the same folder

class UI:
    def __init__(self):
        self.model = model.model2048()
        self.main = tk.Tk()
        self.main.title("2048 with AI")
        self.currBoardUI = []

        self.renderMove()
        self.renderBoard()

        self.main.mainloop()

    def renderMove(self):
        reset = tk.Button(self.main, height=5, width=20, text="Reset Puzzle")
        reset.grid(row=0, column=0, padx=5, pady=5)

        AImode1 = tk.Button(self.main, height=5, width=20, text="AI Mode 1, TBD")
        AImode1.grid(row=0, column=1, padx=5, pady=5)

        AImode2 = tk.Button(self.main, height=5, width=20, text="AI Mode 2, TBD")
        AImode2.grid(row=0, column=2, padx=5, pady=5)

    def renderBoard(self):
        board = self.model.getBoard()
        frame = tk.Frame(self.main, bg="black")
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
                    fg="white"
                )
                cell.grid(row=i, column=j, padx=5, pady=5)  # FIXED: column not col
                holder.append(cell)
            self.currBoardUI.append(holder)

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
    UI()