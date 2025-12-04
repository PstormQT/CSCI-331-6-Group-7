# CSCI-331-6-Group-7
GitHub for the AI class

## Overview
We will be implementing an AI agent to play the 2048 game with 2 different algorithms:
1. Expectiminimax - A modification of minimax with a change to take account into the randomness
2. Monte Carlo tree search - Search Tree that emphasis on expanding the best possible state

Team Members:
- Peter Dang: UI and Monte Carlo
- Katie Richardson: Expectiminimax
- Nathan Russo: Model and Review

## How to play
0. Verify you have installed all dependencies in requirements.txt.
1. Run UI.py to play 2048 or test the AI search algorithms.
    1. Click "Manual Playing" to play normally using the d-pad.
    2. Click "AI Mode 1" to watch the Expectiminimax algorithm attempt to solve 2048.
    3. Click "AI Mode 2" to watch the Monte Carlo algorithm attempt to solve 2048.
2. Run dataRecord.py to analyze our AI search algorithms.
    1. Results for Expectiminimax are found under data in dataReportMinimax.csv.
    2. Results for Monte Carlo are found under data in dataReportMonteCarlo.csv.

## Artificial Intelligence Implementation Techniques
1. Expectiminimax

    We will use a modification of minimax (Expectiminimax) due to the nature of 2048. 
        Technically, there is only one actual player who is "playing the game", so to get 
        around this, we have set the max and min players as follows:

    -   Max Node Player (MaxNP): Normal player who is sliding and merging tiles
    -   Min Node Player (MinNP): The spawning of the 2048 tiles

2. Monte Carlo Tree Search 

    Monte Carlo Search Tree is a search method similar to the Expectiminimax with an 
    emphasis on only expanding on the best state. 
        
    This will run faster and deeper comparing to Expectiminimax due to it doesn't have to
    expand the node that is less valuable