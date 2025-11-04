# CSCI-331-6-Group-7
GitHub for the AI class

We will be completing the 2048 Classic Game


Team Members:
- Peter Dang
- Katie Richardson
- Nathan Russo

General Technique using:
Minimax Implementation  with depth of 5-10


Artificla Intelligence implementation techniques:
1. Expectiminimax with Alpha - Beta Pruning
    -   We will go with a modification of minimax (Expectiminimax) due to the nature of 2048 
        of there is technically one actual player who is  "playing the game" we modify 
        the logic of the Minimax with changing the perspective of who the players are
        -   Max node player: Normal player who is playing the game
        -   Min node player: The spawning of the 2048 tiles

    -   With the randomness nature of the Min node player, expectiminimax will be more optimal
        that all of the value from all of the possible renerated node be considered 
        equally to help mimic the randomness nature of the tile spawning the tiles in 2048

2. Monte Carlo Tree Search 
    -   ~~Peter is still doing research on this but this is understand in general~~

    -   To take into account the randomness of the 2048 tile spawning after movement,
        Monte Carlo search tree concentrating more on searching the best possible movement 
        and expanding it search from that that best state.