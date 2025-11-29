import copy
import model
import math
import random
from node import MonteCarloNode




def getAllLegalMove(model: model.Board2048):
    moves = []
    for direction in range(1,5):
        boardCopy = copy.deepcopy(model)
        ifChange = boardCopy.move(direction)
        if ifChange:
            moves.append(direction)

    return moves
    
def expand(node: MonteCarloNode) -> MonteCarloNode:
    """
    _summary_: The expandsion state for the Monte Carlo Tree search
    Expand 1 of the children node for the game

    Args:
        node (MonteCarloNode): Generate 1 random node (if possible) 
        add into the moveMadeGroup

    Returns:
        MonteCarloNode: The next generation for the leaf node, None if 
        there are not one avaliable
    """

    # Check if current state is dead
    if node.isEnded:
        return None
    
    # Getting all combination moves for the children node
    allMove = getAllLegalMove(node.state)
    allPossibleMove = []

    for move in allMove:
        if move not in node.children:
            allPossibleMove.append(move)

    # No more possible move
    if allPossibleMove == []:
        return None
    
    # Pick a random option, make the new child node then return it
    action = random.choice(allPossibleMove)

    newChild = copy.deepcopy(node.state)
    newChild.playAction(action)

    child = MonteCarloNode(newChild, node, action)
    node.children[action] = child
    return child


def getBestChild(node: MonteCarloNode) -> MonteCarloNode:
    """
    _summary_: Getting the best child using the UCT

    UCT = Xj + C * (sqrt(ln(n) / nj))

    Use https://www.chessprogramming.org/UCT for variable explaination

    Args:
        node (MonteCarloNode): Best Children to expand using UCT score
    """

    bestScore = -float("inf")
    bestAction = None
    bestChild = None

    for action, child in node.children.items():
        # Haven't visit yet
        if child.visitCount == 0:
            UCTScore = float("inf")
        else:
            current = child.totalWeight / child.visitCount
            explorationWeight = math.sqrt(2) * math.sqrt(math.log(node.visitCount) / child.visitCount)

            UCTScore = current + explorationWeight
        
        if UCTScore > bestScore:
            bestScore = UCTScore
            bestAction = action
            bestChild = child

    return bestAction, bestChild


def rollout(state: model.Board2048, limit = 50) -> int:
    """
    _summary_: Single rollout state for the monte carlo tree search.

    Args:
        state (model.Board2048): current baord state
        limit (int, optional): limit of how many interation to run. Defaults to 50.

    Returns:
        int: the current score improvement of the board after the simulation
    """

    sim = copy.deepcopy(state)
    startScore = sim.getScore()

    runCt = 0

    while not sim.getGameOver() and runCt < limit:
        possibleMove = getAllLegalMove(sim)
        
        if possibleMove == []:
            break

        action = random.choice(possibleMove)
        sim.playAction(action)
        runCt += 1

    return sim.getScore() - startScore

def backpropagate(node: MonteCarloNode, reward: float) -> None:
    """
    _summary_: Update the reward for the new node

    Args:
        node (MonteCarloNode): _description_
        reward (float): _description_
    """
    curr = node
    while curr is not None:
        curr.visitCount += 1
        curr.totalWeight += reward
        curr = curr.parent

def getNodeForRollout(root: MonteCarloNode) -> MonteCarloNode:
    """
    _summary_: Get the node for rolling out for MonteCarlo
    Combination for Tree Traveral and expansion

    Args:
        root (MonteCarloNode): Root Node for the MonteCarlo tree

    Returns:
        MonteCarloNode: Best node to expand on
    """

    curr = root
    while not curr.isEnded:
        moves = getAllLegalMove(curr.state)
        if moves == []:
            curr.isEnded = True
            return curr
        
        if set(moves) - set(curr.children):
            return expand(curr) or curr

        action, curr = getBestChild(curr)

    return curr

def getBestActionRoot(root: MonteCarloNode) -> int:
    """
    _summary_: Getting the best action from the root node

    Args:
        root (MonteCarloNode): Root node of the monte carlo tree

    Returns:
        int: direction for the movement
    """

    if not root.children:
        return None
    
    bestAction = None
    bestVisit = -1

    for action, child in root.children.items():
        if child.visitCount > bestVisit:
            bestVisit = child.visitCount
            bestAction = action

    return bestAction


def getBestMove(model: model.Board2048, simulationCount : int = 100, simulationDepth : int = 50) -> int:
    """
    _summary_: Getting the next move for the 2048 using MonteCarco tree search

    Args:
        model (model.Board2048): _description_
        simulationCount (int): _description_

    Returns:
        int: movement direction
    """

    rootState = copy.deepcopy(model)
    root = MonteCarloNode(rootState)

    if rootState.getGameOver():
        return None
    
    for i in range(simulationCount):
        # Select + Expand
        node = getNodeForRollout(root)
        if node == None:
            break
        
        # Rollout
        reward = rollout(node.state, simulationDepth)

        # Backpropagation
        backpropagate(node, reward)

    return getBestActionRoot(root)