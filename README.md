# CSCI-331-6-Group-7
GitHub for the AI class

## Overview
We will be implementing an AI agent to play the 2048 game with 2 different algorithms:
1. Expectiminimax - A modification of minimax with a change to take account into the randomness
2. Monte Carlo tree search - Search Tree that emphasis on expanding the best possible state

Team Members:
- Peter Dang: UI and Monte Carlo
- Katie Richardson: Expectiminmax
- Nathan Russo: Model and Review

## How to play
0. Verify you have installed all dependencies in requirements.txt.
1. Run UI.py to play 2048 or test the AI search algorithms.
    1. Click "Manual Playing" to play normally using the d-pad.
    2. Click "AI Mode 1" to watch the Expectiminmax algorithm attempt to solve 2048.
    3. Click "AI Mode 2" to watch the Monte Carlo algorithm attempt to solve 2048.
2. Run dataRecord.py to analyze our AI search algorithms.
    1. Results for Expectiminmax are found under data in dataReportMinimax.csv.
    2. Results for Monte Carlo are found under data in dataReportMonteCarlo.csv.

## Artificial Intelligence Implementation Techniques
1. Expectiminimax

    It is a a modification of minimax that takes into account randomness.

    -   Max Player (MaxP): Normal player who is sliding and merging tiles. 
    -   Min Player (MinP): The spawning of the 2 and 4 tiles.

2. Monte Carlo Tree Search 

    It is a search tree algorithm that uses simulations of the game board to approximate the best move.

    MCTS works on 4 general steps repeated in order:
    1. Select
    2. Expand
    3. Simulation
    4. Backpropagation