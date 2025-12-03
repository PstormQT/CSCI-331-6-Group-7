import model
import expectiminimax as emm
import montecarlo as mc
import time
import random

"""
Running 2048 and comparing it between the 2 AI
Minimax with depth of 3
Monte Carlo Tree Search with Search depth of 200 and 200 Simulation
"""

# for SEARCH_DEPTH in [2,3,4]:
#     with open(f"expectiminimax/dataReportMinimax{SEARCH_DEPTH}.csv", "w") as file:
#         for x in range(100):
#             start = time.perf_counter()
#             minimaxScore = -1
#             minimaxModel = model.Board2048()
#             while not minimaxModel.getGameOver():
#                 moveMinimax = emm.getNextMove(minimaxModel, SEARCH_DEPTH)
#                 minimaxModel.playAction(moveMinimax)
#             minimaxScore = minimaxModel.getScore()
#             end = time.perf_counter()
#             elapsed_time = end - start
#             file.write(f"{minimaxScore}, {elapsed_time:.4f}\n")

for sim_count in [10,25,40,50,75,100]:
    with open(f"montecarlo/dataReportMonteCarlo{sim_count}.csv", "w") as file:
        for trial in range(100):
            start = time.perf_counter()
            MonteCarloScore = -1

            monteCarloModel = model.Board2048()
            while not monteCarloModel.getGameOver():
                moveMonteCarlo = mc.getBestMove(monteCarloModel, sim_count, sim_count)
                # If monte carlot can't find a node, pick a random one
                if moveMonteCarlo is None:
                    possible = mc.getAllLegalMove(monteCarloModel)
                    if not possible:
                        # Break cause no more move
                        break
                    moveMonteCarlo = random.choice(possible)

                monteCarloModel.playAction(moveMonteCarlo)
            MonteCarloScore = monteCarloModel.getScore()
            end = time.perf_counter()
            elapsed_time = end - start
            file.write(f"{MonteCarloScore}, {elapsed_time:.4f}\n")
