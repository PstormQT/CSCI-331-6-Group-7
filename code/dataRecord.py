import model
import expectiminimax as emm
import montecarlo
import time

"""
Running 2048 and comparing it between the 2 AI
Minimax with depth of 3
Monte Carlo Tree Search with Search depth of 200 and 200 Simulation
"""
SEARCH_DEPTH = 3

with open("dataReportMinimax.csv", "w") as file:
    for x in range(10):
        start = time.perf_counter()
        minimaxScore = -1
        MonteCarloScore = -1
        
        minimaxModel = model.Board2048()
        while not minimaxModel.getGameOver():
            moveMinimax = emm.getNextMove(minimaxModel, SEARCH_DEPTH)
            minimaxModel.playAction(moveMinimax)
        minimaxScore = minimaxModel.getScore()
        end = time.perf_counter()
        elapsed_time = end - start
        file.write(f"{minimaxScore}, {elapsed_time:.4f}\n")

for x in [10,20,50,75,100]:
    with open(f"dataReportMonteCarlo{x}.csv", "w") as file:
        for x in range(10):
            start = time.perf_counter()
            MonteCarloScore = -1
            
            monteCarloModel = model.Board2048()
            while not monteCarloModel.getGameOver():
                moveMonteCarlo = montecarlo.getBestMove(monteCarloModel, x, x)
                monteCarloModel.playAction(moveMonteCarlo)
            MonteCarloScore = monteCarloModel.getScore()
            end = time.perf_counter()
            elapsed_time = end - start
            file.write(f"{MonteCarloScore}, {elapsed_time:.4f}\n")
