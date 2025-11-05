# CSCI-331-6-Group-7
GitHub for the AI class


## Overview
We will be implementing an AI agent to play the 2048 game with 2 different algorithms:
1. Expectiminimax - A modification of minimax with a change to take account into the randomness
2. Monte Carlo tree search - Search Tree that emphasis on expanding the best possible state

Team Members:
- Peter Dang
- Katie Richardson
- Nathan Russo

## Artificial Intelligence Implementation Techniques:
1. Expectiminimax with Alpha - Beta Pruning

    We will use a modification of minimax (Expectiminimax) due to the nature of 2048. 
        Technically, there is only one actual player who is "playing the game", so to get 
        around this, we have set the max and min players as follows:
        -   Max Node Player (MaxNP): Normal player who is sliding and merging tiles
        -   Min Node Player (MinNP): The spawning of the 2048 tiles

    With the randomness of the MinNP, Expectiminimax will be more optimal that all of 
    the value from all of the possible renerated node be considered equally to help 
    mimic the randomness nature of the tile spawning the tiles in 2048.

2. Monte Carlo Tree Search 
    ~~Peter is still doing research on this but this is his understand in general~~

    Monte Carlo Search Tree is a search method similar to the Expectiminimax with an 
    emphasis on only expanding on the best state. 
        
    This will run faster and deeper comparing to Expectiminimax due to it doesn't have to
    expand the node that is less valuable

## Resource used
1. 2048 Game in general 
    -   https://classic.play2048.co/

2. Expectiminimax
    -   https://youtu.be/0fOLkZJ-Q6I?si=xEpKZ95S0Lz_9jlZ
    -   https://github.com/mschrandt/2048
    -   https://stackoverflow.com/questions/22342854/what-is-the-optimal-algorithm-for-the-game-2048
    -   https://inst.eecs.berkeley.edu/~cs188/textbook/games/expectimax.html

3. Monte Carlo Search tree
    -   https://www.geeksforgeeks.org/machine-learning/ml-monte-carlo-tree-search-mcts/
    -   https://en.wikipedia.org/wiki/Monte_Carlo_tree_search
