import model
import ai
import montecarlo
import time

"""
Running 2048 and comparing it between the 2 AI
Minimax with depth of 3
Monte Carlo Tree Search with Search depth of 200 and 200 Simulation
"""
SEARCH_DEPTH = 3
MONTE_CARLO_SIMULATION_COUNT = 200
MONTE_CARLO_SIMULATION_DEPTH = 200

with open("dataReportMinimax.csv", "w") as file:
    for x in range(1):
        start = time.perf_counter()
        minimaxScore = -1
        MonteCarloScore = -1
        
        minimaxModel = model.Board2048()
        while not minimaxModel.getGameOver():
            moveMinimax = ai.getNextMove(minimaxModel, SEARCH_DEPTH)
            minimaxModel.playAction(moveMinimax)
        minimaxScore = minimaxModel.getScore()
        end = time.perf_counter()
        elapsed_time = end - start
        file.write(f"{minimaxScore}, {elapsed_time:.4f}")



with open("dataReportMonteCarlo.csv", "w") as file:
    for x in range(1):
        start = time.perf_counter()
        MonteCarloScore = -1
        
        monteCarloModel = model.Board2048()
        while not monteCarloModel.getGameOver():
            moveMonteCarlo = montecarlo.getBestMove(monteCarloModel, MONTE_CARLO_SIMULATION_COUNT, MONTE_CARLO_SIMULATION_DEPTH)
            monteCarloModel.playAction(moveMonteCarlo)
        MonteCarloScore = monteCarloModel.getScore()
        end = time.perf_counter()
        elapsed_time = end - start
        file.write(f"{MonteCarloScore}, {elapsed_time:.4f}")



