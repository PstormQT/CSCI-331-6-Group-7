# CSCI-331-6-Group-7
GitHub for the AI class


## Overview
We will me implement an AI agent to play the 2048 game with 2 different methods of 
    -   Expectiminimax (A modification of minimax with a change to take account into the randomness)
    -   Monte Carlo tree search (Search Tree that emphasis on expanding the best possible state)

Team Members:
- Peter Dang
- Katie Richardson
- Nathan Russo

## Artificla Intelligence implementation techniques:
1. Expectiminimax with Alpha - Beta Pruning
    -   We will go with a modification of minimax (Expectiminimax) due to the nature of 2048 
        of there is technically one actual player who is  "playing the game" we modify 
        the logic of the Minimax with changing the perspective of who the players are into this perspective:
        -   Max node player: Normal player who is playing the game
        -   Min node player: The spawning of the 2048 tiles

    -   With the randomness nature of the Min node player, expectiminimax will be more optimal
        that all of the value from all of the possible renerated node be considered 
        equally to help mimic the randomness nature of the tile spawning the tiles in 2048.

2. Monte Carlo Tree Search 
    -   ~~Peter is still doing research on this but this is his understand in general~~

    -   Monte Carlo search tree is a search method similar to the expectiminimax with an 
        emphasis on only expanding on the best state. This will help optimizing on that it doesn't 
        have to simulate all of the board state for each additional movement that was made.

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